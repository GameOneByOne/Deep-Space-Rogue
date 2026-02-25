const CLIENT_ID_KEY = "dsr_client_id";
const params = new URLSearchParams(location.search);
const DEFAULT_API_BASE = (() => {
  if (window.DSR_API_BASE) return window.DSR_API_BASE;
  if (location.protocol === "file:") return "http://127.0.0.1:8000";
  // Railway 部署地址
  return "https://web-production-92a08.up.railway.app";
})();
const API_BASE = params.get("api") || DEFAULT_API_BASE;

function generateClientId() {
  if (typeof crypto !== "undefined" && crypto.randomUUID) {
    return crypto.randomUUID();
  }
  return `client_${Math.random().toString(36).slice(2, 10)}`;
}

let clientId = params.get("clientId") || localStorage.getItem(CLIENT_ID_KEY);
if (!clientId) {
  clientId = generateClientId();
  localStorage.setItem(CLIENT_ID_KEY, clientId);
}

const els = {
  resources: document.getElementById("resource-list"),
  buildings: document.getElementById("building-list"),
  events: document.getElementById("event-list"),
  professions: document.getElementById("profession-list"),
  researches: document.getElementById("research-list"),
  tooltip: document.getElementById("tooltip"),
  status: document.getElementById("status-text"),
  toastStack: document.getElementById("toast-stack"),
};

function setStatus(text) {
  if (!els.status) return;
  els.status.textContent = text || "";
}

function fnum(value) {
  const n = Number(value ?? 0);
  const s = n.toFixed(3);
  return s.replace(/\.?0+$/, "");
}

function setTip(el, text) {
  el.dataset.tip = text || "";
}

function showToast(title, message, type = "info", ttl = 2400) {
  if (!els.toastStack) return;
  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  const titleEl = document.createElement("div");
  titleEl.className = "toast-title";
  titleEl.textContent = title;
  const msgEl = document.createElement("div");
  msgEl.className = "toast-sub";
  msgEl.textContent = message || "";
  toast.appendChild(titleEl);
  toast.appendChild(msgEl);
  els.toastStack.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, ttl);
}

async function apiRequest(path, options = {}) {
  const headers = new Headers(options.headers || {});
  headers.set("X-Client-Id", clientId);
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if (!res.ok) {
    const msg = await res.text().catch(() => "");
    throw new Error(`${res.status} ${res.statusText} ${msg}`.trim());
  }
  return res;
}

async function apiJson(path, options = {}) {
  const res = await apiRequest(path, options);
  if (res.status === 204) return null;
  return await res.json();
}

let refreshInFlight = false;
let refreshQueued = false;
let currentState = null;

async function refreshState() {
  if (refreshInFlight) {
    refreshQueued = true;
    return;
  }
  refreshInFlight = true;
  try {
    const data = await apiJson("/state");
    currentState = data || null;
    render(currentState || {});
    setStatus(`在线 | Client: ${clientId}`);
  } catch (err) {
    setStatus(`连接失败: ${String(err)}`);
  } finally {
    refreshInFlight = false;
    if (refreshQueued) {
      refreshQueued = false;
      refreshState();
    }
  }
}

async function postAction(path) {
  try {
    await apiJson(path, { method: "POST" });
    // showToast("操作完成", path, "success");
  } catch (err) {
    // setStatus(`操作失败: ${String(err)}`);
    // showToast("操作失败", String(err), "error", 3200);
  } finally {
    refreshState();
  }
}

function buildNameMap(resources, buildings, professions, researches) {
  const map = new Map();
  resources.forEach((r) => map.set(r.id, r.name));
  buildings.forEach((b) => map.set(b.id, b.name));
  professions.forEach((p) => map.set(p.id, p.name));
  researches.forEach((r) => map.set(r.id, r.name));
  return (id) => map.get(id) || id;
}

function renderResources(resources) {
  els.resources.innerHTML = "";
  resources.forEach((r) => {
    const row = document.createElement("div");
    row.className = "resource-item";
    const rate = Number(r.rate || 0);
    const rateClass = rate > 0 ? "pos" : rate < 0 ? "neg" : "zero";
    row.innerHTML = `<span>${r.name} ${fnum(r.count)}/${fnum(r.limit)}</span>
      <span class="resource-rate ${rateClass}">${rate >= 0 ? "+" : ""}${rate.toFixed(2)}</span>`;
    setTip(row, `【资源】${r.name}\n${r.desc || ""}`);
    els.resources.appendChild(row);
  });
}

function renderBuildings(buildings, nameOf, dontChangeButtonStatus = false) {
  const exist = els.buildings.querySelectorAll("[data-id]");
  const existMap = new Map();
  exist.forEach((node) => {
    existMap.set(node.dataset.id, node);
  });
  const seen = new Set();
  buildings.forEach((b) => {
    let btn = existMap.get(b.id);
    const isNew = !btn;
    if (!btn) {
      btn = document.createElement("button");
      btn.className = "btn";
      btn.dataset.id = b.id;
    }

    if (!dontChangeButtonStatus) {
      btn.disabled = !b.canBuild;
    }
    const nextText = b.count > 0 ? `${b.name}(${b.count})` : b.name;
    if (btn.textContent !== nextText) {
      btn.textContent = nextText;
    }
    if (isNew) {
      btn.addEventListener("click", () => postAction(`/build/${encodeURIComponent(b.id)}`));
    }
    const costText = (b.costDesc || []).join("\n");
    const effectText = (b.effectsDesc || []).join("\n");
    let tip = `【建筑】${b.name}\n${b.desc || ""}\n`;
    if (costText) tip += `\n【建造消耗】\n${costText}\n`;
    tip += `\n【效果】\n${effectText || "无"}`;
    setTip(btn, tip);
    if (isNew) {
      els.buildings.appendChild(btn);
    }
    seen.add(b.id);
  });

  existMap.forEach((node, id) => {
    if (!seen.has(id)) node.remove();
  });
}

function renderEvents(events) {
  if (!els.events) return;
  const exist = els.events.querySelectorAll("[data-id]");
  const existMap = new Map();
  exist.forEach((node) => {
    existMap.set(node.dataset.id, node);
  });
  const seen = new Set();
  events.forEach((ev) => {
    let label = existMap.get(ev.id);
    const isNew = !label;
    if (!label) {
      label = document.createElement("div");
      label.className = "event-label";
      label.dataset.id = ev.id;
    }
    if (label.textContent !== ev.name) {
      label.textContent = ev.name;
    }
    const effects = (ev.effects || []).join("\n");
    let tip = `【事件】${ev.name}\n${ev.desc || ""}\n`;
    if (typeof ev.weight !== "undefined") {
      tip += `\n【权重】${ev.weight}`;
    }
    if (typeof ev.cooldown !== "undefined") {
      tip += `\n【冷却】${ev.cooldown}`;
    }
    if (effects) {
      tip += `\n\n【效果】\n${effects}`;
    }
    setTip(label, tip);
    if (isNew) {
      els.events.appendChild(label);
    }
    seen.add(ev.id);
  });

  existMap.forEach((node, id) => {
    if (!seen.has(id)) node.remove();
  });
}

function renderProfessions(professions) {
  els.professions.innerHTML = "";
  const idle = professions.find((p) => p.id === "P_IDLE");
  const idleCount = idle ? Number(idle.count || 0) : 0;

  professions.forEach((p) => {
    const row = document.createElement("div");
    row.className = "profession-row";
    const name = document.createElement("div");
    name.className = "profession-name";
    if (p.limit < 0) {
      name.textContent = `${p.name}: ${p.count}`;
    } else {
      name.textContent = `${p.name}: ${p.count}/${p.limit}`;
    }

    const ops = document.createElement("div");
    ops.className = "ops";
    if (p.canEdit) {
      const add = document.createElement("button");
      add.className = "op-btn";
      add.textContent = "+";
      const canAdd = idleCount > 0 && (p.limit < 0 || p.count < p.limit);
      add.disabled = !canAdd;
      add.addEventListener("click", () => postAction(`/dispatch/${encodeURIComponent("P_IDLE")}/${encodeURIComponent(p.id)}`));
      ops.appendChild(add);

      const sub = document.createElement("button");
      sub.className = "op-btn";
      sub.textContent = "-";
      const canSub = p.count > 0;
      sub.disabled = !canSub;
      sub.addEventListener("click", () => postAction(`/undispatch/${encodeURIComponent(p.id)}/${encodeURIComponent("P_IDLE")}`));
      ops.appendChild(sub);
    }

    row.appendChild(name);
    row.appendChild(ops);
    const effects = (p.effectsDesc || []).join("\n") || "无";
    setTip(row, `【人力】${p.name}\n${p.desc || ""}\n\n【效果】\n${effects}`);
    els.professions.appendChild(row);
  });
}

function renderResearches(researches, nameOf, dontChangeButtonStatus = false) {
  const exist = els.researches.querySelectorAll("[data-id]");
  const existMap = new Map();
  exist.forEach((node) => {
    existMap.set(node.dataset.id, node);
  });
  const seen = new Set();
  researches.forEach((r) => {
    let btn = existMap.get(r.id);
    const isNew = !btn;
    if (!btn) {
      btn = document.createElement("button");
      btn.className = "btn";
      btn.dataset.id = r.id;
    }
    const nextText = r.finished ? `${r.name}(已完成)` : r.name;
    if (btn.textContent !== nextText) {
      btn.textContent = nextText;
    }
    if (!dontChangeButtonStatus) {
      btn.disabled = !!r.finished || r.canResearch === false;
    }
    if (isNew) {
      btn.addEventListener("click", () => postAction(`/research/${encodeURIComponent(r.id)}`));
    }
    const costText = (r.costDesc || []).join("\n");
    const effects = (r.effectsDesc || []).join("\n");
    let tip = `【研究】${r.name}\n${r.desc || ""}\n`;
    if (costText) tip += `\n【研究消耗】\n${costText}\n`;
    if (effects) tip += `\n【效果】\n${effects}`;
    setTip(btn, tip);
    if (isNew) {
      els.researches.appendChild(btn);
    }
    seen.add(r.id);
  });

  existMap.forEach((node, id) => {
    if (!seen.has(id)) node.remove();
  });
}

function render(state) {
  const resources = Object.values(state.resources || {});
  const buildings = Object.values(state.buildings || {});
  const professions = Object.values(state.professions || {});
  const researches = Object.values(state.research || {});
  const events = Object.values(state.events || {});
  const nameOf = buildNameMap(resources, buildings, professions, researches);

  renderResources(resources);
  renderBuildings(buildings, nameOf, true);
  renderEvents(events);
  renderProfessions(professions);
  renderResearches(researches, nameOf, true);
}

function applyLocalResourceTick(seconds = 1) {
  if (!currentState) return;
  const resources = Object.values(currentState.resources || {});
  resources.forEach((r) => {
    const rate = Number(r.rate || 0);
    const limit = Number(r.limit ?? r.count ?? 0);
    const next = Number(r.count || 0) + rate * seconds;
    r.count = Math.max(0, Math.min(limit, next));
  });
  const resMap = new Map(resources.map((r) => [r.id, r]));
  const isEnough = (cost = []) =>
    (cost || []).every((c) => (resMap.get(c.id)?.count ?? 0) >= (c.need ?? 0));

  const buildings = Object.values(currentState.buildings || {});
  let buildingChanged = false;
  buildings.forEach((b) => {
    const next = isEnough(b.cost || []);
    if (b.canBuild !== next) buildingChanged = true;
    b.canBuild = next;
  });

  const researches = Object.values(currentState.research || {});
  let researchChanged = false;
  researches.forEach((r) => {
    const next = isEnough(r.cost || []);
    if (r.canResearch !== next) researchChanged = true;
    r.canResearch = next;
  });

  const professions = Object.values(currentState.professions || {});
  const nameOf = buildNameMap(resources, buildings, professions, researches);
  renderResources(resources);
  if (buildingChanged) renderBuildings(buildings, nameOf);
  if (researchChanged) renderResearches(researches, nameOf);
}

function bindTooltip() {
  document.addEventListener("mousemove", (e) => {
    const host = e.target.closest("[data-tip]");
    if (!host || !host.dataset.tip) {
      els.tooltip.classList.add("hidden");
      return;
    }
    els.tooltip.textContent = host.dataset.tip;
    els.tooltip.classList.remove("hidden");
    els.tooltip.style.left = `${e.clientX + 14}px`;
    els.tooltip.style.top = `${e.clientY + 14}px`;
  });
  document.addEventListener("mouseleave", () => {
    els.tooltip.classList.add("hidden");
  });
}

function startEventStream() {
  if (typeof EventSource === "undefined") return;
  const base = API_BASE || "";
  const url = `${base}/events?clientId=${encodeURIComponent(clientId)}`;
  const es = new EventSource(url);
  es.onmessage = (e) => {
    refreshState();
    try {
      const payload = JSON.parse(e.data);
      const title = payload.type ? `事件: ${payload.type}` : "事件";
      const detail = payload.buildingId || payload.researchId || payload.toProfessionId || "";
      showToast(title, detail, "info");
    } catch {
      showToast("事件", "收到通知", "info");
    }
  };
  es.onerror = () => {
    setStatus("SSE 连接中断，重试中...");
  };
}

function boot() {
  bindTooltip();
  refreshState();
  startEventStream();
  setInterval(() => applyLocalResourceTick(1), 1000);
}

boot();
