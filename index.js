const SAVE_KEY = "dsr_local_save_v2";

const EMBEDDED_DATA = {
  "resources": [
    {
      "id": "R_KNOWLEDGE",
      "name": "知识",
      "desc": "用于研究和升级",
      "defaultUnlock": false,
      "defaultCapacity": 100
    },
    {
      "id": "R_FOOD",
      "name": "食物",
      "desc": "用于生存与烹饪",
      "defaultUnlock": true,
      "defaultCapacity": 80
    },
    {
      "id": "R_RATION",
      "name": "口粮",
      "desc": "加工后的高效食物，促进人口增长",
      "defaultUnlock": false,
      "defaultCapacity": 50
    },
    {
      "id": "R_WOOD",
      "name": "木材",
      "desc": "用于建造与加工",
      "defaultUnlock": true,
      "defaultCapacity": 50
    },
    {
      "id": "R_STONE",
      "name": "石头",
      "desc": "用于建造与升级",
      "defaultUnlock": true,
      "defaultCapacity": 50
    },
    {
      "id": "R_ANIMAL_HIDE",
      "name": "兽皮",
      "desc": "用于保暖",
      "defaultUnlock": true,
      "defaultCapacity": 20
    },
    {
      "id": "R_CROP",
      "name": "农作物",
      "desc": "农业产出的粮食作物",
      "defaultUnlock": false,
      "defaultCapacity": 80
    },
    {
      "id": "R_FABRIC",
      "name": "布匹",
      "desc": "用于制作衣物",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_METAL_ORE",
      "name": "金属矿石",
      "desc": "含有金属的原始矿石",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_METAL",
      "name": "金属锭",
      "desc": "冶炼后的可用金属",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_TOOLS",
      "name": "工具",
      "desc": "提高工作效率的器具",
      "defaultUnlock": false,
      "defaultCapacity": 25
    },
    {
      "id": "R_COAL",
      "name": "煤炭",
      "desc": "工业时代的燃料",
      "defaultUnlock": false,
      "defaultCapacity": 80
    },
    {
      "id": "R_STEEL",
      "name": "钢铁",
      "desc": "高强度建筑材料",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_PARTS",
      "name": "机械零件",
      "desc": "机械装置的组件",
      "defaultUnlock": false,
      "defaultCapacity": 30
    },
    {
      "id": "R_MACHINERY",
      "name": "机械设备",
      "desc": "复杂的机械装置",
      "defaultUnlock": false,
      "defaultCapacity": 20
    },
    {
      "id": "R_ELECTRICITY",
      "name": "电力",
      "desc": "电气时代的能量来源",
      "defaultUnlock": false,
      "defaultCapacity": 300
    },
    {
      "id": "R_OIL",
      "name": "石油",
      "desc": "液态化石燃料",
      "defaultUnlock": false,
      "defaultCapacity": 80
    },
    {
      "id": "R_PLASTIC",
      "name": "塑料",
      "desc": "合成材料",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_CIRCUIT",
      "name": "电路板",
      "desc": "电子设备的基板",
      "defaultUnlock": false,
      "defaultCapacity": 25
    },
    {
      "id": "R_URANIUM",
      "name": "铀矿石",
      "desc": "放射性矿物",
      "defaultUnlock": false,
      "defaultCapacity": 25
    },
    {
      "id": "R_ENRICHED_URANIUM",
      "name": "浓缩铀",
      "desc": "核能燃料",
      "defaultUnlock": false,
      "defaultCapacity": 15
    },
    {
      "id": "R_NUCLEAR_ENERGY",
      "name": "核能",
      "desc": "强大的能源",
      "defaultUnlock": false,
      "defaultCapacity": 600
    },
    {
      "id": "R_ROCKET_FUEL",
      "name": "火箭燃料",
      "desc": "高能推进剂",
      "defaultUnlock": false,
      "defaultCapacity": 40
    },
    {
      "id": "R_ALLOY",
      "name": "航天合金",
      "desc": "轻量化高强度材料",
      "defaultUnlock": false,
      "defaultCapacity": 30
    },
    {
      "id": "R_CHIP",
      "name": "芯片",
      "desc": "高级计算元件",
      "defaultUnlock": false,
      "defaultCapacity": 15
    },
    {
      "id": "R_LIFE_SUPPORT",
      "name": "生命维持",
      "desc": "太空生存必需品",
      "defaultUnlock": false,
      "defaultCapacity": 25
    },
    {
      "id": "R_ANTIMATTER",
      "name": "反物质",
      "desc": "终极能源",
      "defaultUnlock": false,
      "defaultCapacity": 8
    },
    {
      "id": "R_DARK_ENERGY",
      "name": "暗能量",
      "desc": "宇宙的神秘力量",
      "defaultUnlock": false,
      "defaultCapacity": 4
    },
    {
      "id": "R_ALIEN_TECH",
      "name": "外星科技",
      "desc": "来自其他文明的技术",
      "defaultUnlock": false,
      "defaultCapacity": 8
    }
  ],
  "buildings": [
    {
      "id": "B_CAMPFIRE",
      "name": "篝火",
      "desc": "提供热量与光明；推动人口增长与知识萌芽",
      "defaultUnlock": true,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 5
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_IDLE",
          "count": 3
        },
        {
          "type": "add",
          "target": "profession",
          "id": "P_IDLE",
          "count": 3,
          "per": "click"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_KNOWLEDGE"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_FARMLAND"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_HUNTING_CAMP"
        }
      ]
    },
    {
      "id": "B_FARMLAND",
      "name": "开垦地",
      "desc": "需要农夫工作才产出食物（分工起点）",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 5
        },
        {
          "id": "R_FOOD",
          "need": 3
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_FARMER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_FARMER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_LUMBER_CAMP"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_QUARRY"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_CROP"
        }
      ]
    },
    {
      "id": "B_LUMBER_CAMP",
      "name": "伐木营地",
      "desc": "稳定产出木材",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 8
        },
        {
          "id": "R_FOOD",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_LUMBERJACK"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_LUMBERJACK",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_HUNTING_CAMP"
        }
      ]
    },
    {
      "id": "B_HUNTING_CAMP",
      "name": "猎人小屋",
      "desc": "提供猎人的岗位，稳定获取食物和兽皮",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 10
        },
        {
          "id": "R_STONE",
          "need": 3
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_HUNTER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_HUNTER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_KITCHEN"
        }
      ]
    },
    {
      "id": "B_QUARRY",
      "name": "磨石营地",
      "desc": "产出石头（工程线门票）",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 8
        },
        {
          "id": "R_FOOD",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_QUARRYMAN"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_QUARRYMAN",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_CELLAR"
        }
      ]
    },
    {
      "id": "B_CELLAR",
      "name": "储藏坑",
      "desc": "能增加物资储备",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 6
        },
        {
          "id": "R_STONE",
          "need": 6
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "addLimit",
          "target": "resource",
          "id": "R_FOOD",
          "count": 50
        },
        {
          "type": "addLimit",
          "target": "resource",
          "id": "R_WOOD",
          "count": 30
        },
        {
          "type": "addLimit",
          "target": "resource",
          "id": "R_STONE",
          "count": 30
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_HUT"
        }
      ]
    },
    {
      "id": "B_HUT",
      "name": "茅草屋",
      "desc": "提供基本的居住空间",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 12
        },
        {
          "id": "R_STONE",
          "need": 4
        },
        {
          "id": "R_FOOD",
          "need": 8
        }
      ],
      "effects": [
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_IDLE",
          "count": 5
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_PASTURE"
        }
      ]
    },
    {
      "id": "B_PASTURE",
      "name": "牧场",
      "desc": "驯养动物获取资源",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 15
        },
        {
          "id": "R_FOOD",
          "need": 25
        },
        {
          "id": "R_RATION",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_HERDER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_HERDER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_FABRIC"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_LOOM"
        }
      ]
    },
    {
      "id": "B_LOOM",
      "name": "织布机",
      "desc": "将原材料加工成布匹",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 15
        },
        {
          "id": "R_STONE",
          "need": 6
        },
        {
          "id": "R_FABRIC",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_WEAVER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_WEAVER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_MINE"
        }
      ]
    },
    {
      "id": "B_MINE",
      "name": "矿洞",
      "desc": "深入地下开采矿石",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 20
        },
        {
          "id": "R_STONE",
          "need": 15
        },
        {
          "id": "R_TOOLS",
          "need": 3
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_MINER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_MINER",
          "count": 3
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_METAL_ORE"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_COAL"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_WORKSHOP"
        }
      ]
    },
    {
      "id": "B_WORKSHOP",
      "name": "工坊",
      "desc": "制作工具和简单器具",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_WOOD",
          "need": 25
        },
        {
          "id": "R_STONE",
          "need": 12
        },
        {
          "id": "R_METAL",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_CRAFTSMAN"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_CRAFTSMAN",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_TOOLS"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_SMELTER"
        }
      ]
    },
    {
      "id": "B_SMELTER",
      "name": "冶炼炉",
      "desc": "将矿石冶炼成可用金属",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STONE",
          "need": 25
        },
        {
          "id": "R_COAL",
          "need": 15
        },
        {
          "id": "R_METAL_ORE",
          "need": 10
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_SMELTER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_SMELTER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_METAL"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_STEEL_MILL"
        }
      ]
    },
    {
      "id": "B_STEEL_MILL",
      "name": "炼钢厂",
      "desc": "生产高强度钢材",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_METAL",
          "need": 25
        },
        {
          "id": "R_COAL",
          "need": 35
        },
        {
          "id": "R_STONE",
          "need": 30
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_STEELWORKER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_STEELWORKER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_STEEL"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_FACTORY"
        }
      ]
    },
    {
      "id": "B_FACTORY",
      "name": "工厂",
      "desc": "大规模生产机械零件",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 20
        },
        {
          "id": "R_METAL",
          "need": 30
        },
        {
          "id": "R_COAL",
          "need": 50
        },
        {
          "id": "R_TOOLS",
          "need": 10
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_MACHINIST"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_MACHINIST",
          "count": 3
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_PARTS"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_POWER_PLANT"
        }
      ]
    },
    {
      "id": "B_POWER_PLANT",
      "name": "发电厂",
      "desc": "将化学能转化为电能",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 30
        },
        {
          "id": "R_PARTS",
          "need": 20
        },
        {
          "id": "R_COAL",
          "need": 60
        },
        {
          "id": "R_TOOLS",
          "need": 15
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_ELECTRICITY"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 15,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_REFINERY"
        }
      ]
    },
    {
      "id": "B_REFINERY",
      "name": "炼油厂",
      "desc": "提炼石油并生产化工产品",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 35
        },
        {
          "id": "R_PARTS",
          "need": 25
        },
        {
          "id": "R_ELECTRICITY",
          "need": 80
        },
        {
          "id": "R_MACHINERY",
          "need": 5
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_CHEMIST"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_CHEMIST",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_OIL"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_PLASTIC"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ELECTRONICS_PLANT"
        }
      ]
    },
    {
      "id": "B_ELECTRONICS_PLANT",
      "name": "电子工厂",
      "desc": "生产电路板和电子设备",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 25
        },
        {
          "id": "R_PLASTIC",
          "need": 30
        },
        {
          "id": "R_ELECTRICITY",
          "need": 150
        },
        {
          "id": "R_METAL",
          "need": 20
        },
        {
          "id": "R_PARTS",
          "need": 15
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_ENGINEER"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_ENGINEER",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_CIRCUIT"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_TECH_CENTER"
        }
      ]
    },
    {
      "id": "B_TECH_CENTER",
      "name": "科技中心",
      "desc": "进行高级研究",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 50
        },
        {
          "id": "R_CIRCUIT",
          "need": 25
        },
        {
          "id": "R_ELECTRICITY",
          "need": 300
        },
        {
          "id": "R_KNOWLEDGE",
          "need": 150
        },
        {
          "id": "R_PARTS",
          "need": 30
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_TECHNICIAN"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_TECHNICIAN",
          "count": 3
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 8,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_NUCLEAR_PLANT"
        }
      ]
    },
    {
      "id": "B_NUCLEAR_PLANT",
      "name": "核电站",
      "desc": "利用核能产生巨大能量",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 80
        },
        {
          "id": "R_CIRCUIT",
          "need": 50
        },
        {
          "id": "R_ELECTRICITY",
          "need": 500
        },
        {
          "id": "R_URANIUM",
          "need": 10
        },
        {
          "id": "R_CHIP",
          "need": 10
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_PHYSICIST"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_PHYSICIST",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_URANIUM"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_ENRICHED_URANIUM"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_NUCLEAR_ENERGY"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_NUCLEAR_ENERGY",
          "count": 30,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ROCKET_SILO"
        }
      ]
    },
    {
      "id": "B_ROCKET_SILO",
      "name": "火箭发射井",
      "desc": "发射航天器进入太空",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 100
        },
        {
          "id": "R_ALLOY",
          "need": 60
        },
        {
          "id": "R_ROCKET_FUEL",
          "need": 150
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 300
        },
        {
          "id": "R_CHIP",
          "need": 20
        },
        {
          "id": "R_MACHINERY",
          "need": 15
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_ASTRONAUT"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_ASTRONAUT",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_PILOT"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_PILOT",
          "count": 1
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_LIFE_SUPPORT"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ALLOY_WORKS"
        }
      ]
    },
    {
      "id": "B_ALLOY_WORKS",
      "name": "合金工厂",
      "desc": "生产航天级合金材料",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_STEEL",
          "need": 60
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 200
        },
        {
          "id": "R_CIRCUIT",
          "need": 40
        },
        {
          "id": "R_MACHINERY",
          "need": 10
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_ALLOY_SMITH"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_ALLOY_SMITH",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_ALLOY"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_CHIP_FAB"
        }
      ]
    },
    {
      "id": "B_CHIP_FAB",
      "name": "芯片工厂",
      "desc": "制造高精度计算芯片",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_ALLOY",
          "need": 50
        },
        {
          "id": "R_PLASTIC",
          "need": 60
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 400
        },
        {
          "id": "R_CIRCUIT",
          "need": 60
        },
        {
          "id": "R_MACHINERY",
          "need": 15
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_CHIP"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_CHIP",
          "count": 0.8,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_SPACE_STATION"
        }
      ]
    },
    {
      "id": "B_SPACE_STATION",
      "name": "空间站",
      "desc": "近地轨道上的前哨基地",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_ALLOY",
          "need": 120
        },
        {
          "id": "R_CHIP",
          "need": 50
        },
        {
          "id": "R_ROCKET_FUEL",
          "need": 250
        },
        {
          "id": "R_LIFE_SUPPORT",
          "need": 60
        },
        {
          "id": "R_MACHINERY",
          "need": 25
        }
      ],
      "effects": [
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_ASTRONAUT",
          "count": 5
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 15,
          "per": "turn"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ANTIMATTER_LAB"
        }
      ]
    },
    {
      "id": "B_ANTIMATTER_LAB",
      "name": "反物质实验室",
      "desc": "研究宇宙终极能源",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_ALLOY",
          "need": 180
        },
        {
          "id": "R_CHIP",
          "need": 100
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 700
        },
        {
          "id": "R_ANTIMATTER",
          "need": 5
        },
        {
          "id": "R_MACHINERY",
          "need": 30
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_QUANTUM_PHYSICIST"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_QUANTUM_PHYSICIST",
          "count": 2
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_ANTIMATTER"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_DARK_ENERGY"
        },
        {
          "type": "unlock",
          "target": "building",
          "id": "B_INTERSTELLAR_GATE"
        }
      ]
    },
    {
      "id": "B_INTERSTELLAR_GATE",
      "name": "星际之门",
      "desc": "通往其他星系的传送装置",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_ALLOY",
          "need": 400
        },
        {
          "id": "R_CHIP",
          "need": 200
        },
        {
          "id": "R_ANTIMATTER",
          "need": 30
        },
        {
          "id": "R_DARK_ENERGY",
          "need": 15
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 1000
        },
        {
          "id": "R_MACHINERY",
          "need": 50
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_XENOBIOLOGIST"
        },
        {
          "type": "addLimit",
          "target": "profession",
          "id": "P_XENOBIOLOGIST",
          "count": 3
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_ALIEN_TECH"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 30,
          "per": "turn"
        }
      ]
    }
  ],
  "professions":   [
    {
      "id": "P_IDLE",
      "name": "闲置",
      "desc": "未分配工作的居民，人口增长的基础",
      "defaultUnlock": true,
      "editable": false,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_WOOD",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_STONE",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_HUNTER",
      "name": "猎人",
      "desc": "稳定获取食物和兽皮",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": 1.2,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ANIMAL_HIDE",
          "count": 0.3,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.01,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.14,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_FARMER",
      "name": "农夫",
      "desc": "种植农作物",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_CROP",
          "count": 1.8,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.01,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_LUMBERJACK",
      "name": "伐木工",
      "desc": "稳定产出木材",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_WOOD",
          "count": 2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.02,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.18,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_QUARRYMAN",
      "name": "采石工",
      "desc": "开采石头",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_STONE",
          "count": 1.8,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.02,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.18,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_HERDER",
      "name": "牧民",
      "desc": "驯养动物获取资源",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ANIMAL_HIDE",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_FABRIC",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_RATION",
          "count": 0.1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.12,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_WEAVER",
      "name": "织工",
      "desc": "将兽皮制成布匹",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_FABRIC",
          "count": 1.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_ANIMAL_HIDE",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.08,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_MINER",
      "name": "矿工",
      "desc": "开采地下矿石",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_METAL_ORE",
          "count": 1.2,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_COAL",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.03,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.2,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_CRAFTSMAN",
      "name": "工匠",
      "desc": "制作工具和器具",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_METAL",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_WOOD",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.12,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_SMELTER",
      "name": "冶炼工",
      "desc": "将矿石冶炼成金属",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_METAL",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_METAL_ORE",
          "count": 1.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_COAL",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.14,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_STEELWORKER",
      "name": "炼钢工",
      "desc": "生产高强度钢材",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_STEEL",
          "count": 0.8,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_METAL",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_COAL",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.18,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_MACHINIST",
      "name": "机械师",
      "desc": "制造机械零件",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_PARTS",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_MACHINERY",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_STEEL",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_TOOLS",
          "count": 0.1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.16,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_ENGINEER",
      "name": "工程师",
      "desc": "设计和维护复杂设备",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 3,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_CIRCUIT",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_PLASTIC",
          "count": 0.3,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_CHEMIST",
      "name": "化学家",
      "desc": "研究化学工艺",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_PLASTIC",
          "count": 0.8,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ROCKET_FUEL",
          "count": 0.5,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_OIL",
          "count": 0.6,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_PHYSICIST",
      "name": "物理学家",
      "desc": "研究核能与高能物理",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 5,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ENRICHED_URANIUM",
          "count": 0.15,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_URANIUM",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 3,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_TECHNICIAN",
      "name": "技术员",
      "desc": "维护电力和自动化设备",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 8,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_CHIP",
          "count": 0.3,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_CIRCUIT",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_MACHINERY",
          "count": 0.05,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_ASTRONAUT",
      "name": "宇航员",
      "desc": "接受专业训练的太空人员",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 2,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_LIFE_SUPPORT",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_RATION",
          "count": 0.2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_ELECTRICITY",
          "count": 2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.16,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_PILOT",
      "name": "飞行员",
      "desc": "驾驶飞船的专业人员",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 2,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_RATION",
          "count": 0.15,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.12,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_ALLOY_SMITH",
      "name": "合金工匠",
      "desc": "制造航天级合金材料",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_ALLOY",
          "count": 0.5,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_STEEL",
          "count": 0.4,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_NUCLEAR_ENERGY",
          "count": 1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.14,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_XENOBIOLOGIST",
      "name": "外星生物学家",
      "desc": "研究外星生命和生态系统",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 6,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ALIEN_TECH",
          "count": 0.15,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_LIFE_SUPPORT",
          "count": 0.1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    },
    {
      "id": "P_QUANTUM_PHYSICIST",
      "name": "量子物理学家",
      "desc": "研究反物质和暗能量",
      "defaultUnlock": false,
      "editable": true,
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 8,
          "per": "turn"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_ANTIMATTER",
          "count": 0.08,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_NUCLEAR_ENERGY",
          "count": 3,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_CHIP",
          "count": 0.1,
          "per": "turn"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 0.1,
          "per": "turn"
        }
      ]
    }
  ],
  "researches": [
    {
      "id": "T_BASIC_ENGINEERING",
      "name": "基础工程",
      "desc": "建立最初的工程认知，解锁采石场与后续工业研究。",
      "defaultUnlock": true,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 10
        }
      ],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_QUARRY"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_HUNTING"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_AGRICULTURE"
        }
      ]
    },
    {
      "id": "T_HUNTING",
      "name": "狩猎技巧",
      "desc": "掌握协作狩猎，获得稳定食物来源。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 8
        },
        {
          "id": "R_FOOD",
          "need": 8
        },
        {
          "id": "R_ANIMAL_HIDE",
          "need": 3
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "profession",
          "id": "P_HUNTER"
        },
        {
          "type": "professionRateBuff",
          "target": "profession",
          "id": "P_HUNTER",
          "count": 0.3,
          "per": "turn"
        }
      ]
    },
    {
      "id": "T_AGRICULTURE",
      "name": "农业技术",
      "desc": "学会种植作物，食物来源更加稳定。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 15
        },
        {
          "id": "R_WOOD",
          "need": 15
        },
        {
          "id": "R_FOOD",
          "need": 10
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_FARMLAND"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_ANIMAL_HUSBANDRY"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_FOOD_PROCESSING"
        }
      ]
    },
    {
      "id": "T_FOOD_PROCESSING",
      "name": "食物加工",
      "desc": "学会制作口粮，提高食物效率。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 12
        },
        {
          "id": "R_FOOD",
          "need": 15
        },
        {
          "id": "R_STONE",
          "need": 10
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_KITCHEN"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_RATION"
        }
      ]
    },
    {
      "id": "T_ANIMAL_HUSBANDRY",
      "name": "畜牧技术",
      "desc": "驯养动物获取持续资源。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 18
        },
        {
          "id": "R_FOOD",
          "need": 25
        },
        {
          "id": "R_ANIMAL_HIDE",
          "need": 8
        },
        {
          "id": "R_RATION",
          "need": 5
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_PASTURE"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_TEXTILE"
        }
      ]
    },
    {
      "id": "T_TEXTILE",
      "name": "纺织技术",
      "desc": "将兽皮加工成布匹。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 22
        },
        {
          "id": "R_FABRIC",
          "need": 15
        },
        {
          "id": "R_ANIMAL_HIDE",
          "need": 10
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_LOOM"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_MINING"
        }
      ]
    },
    {
      "id": "T_MINING",
      "name": "采矿技术",
      "desc": "深入地下开采有价值的矿石。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 30
        },
        {
          "id": "R_STONE",
          "need": 40
        },
        {
          "id": "R_TOOLS",
          "need": 8
        },
        {
          "id": "R_WOOD",
          "need": 20
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_MINE"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_METALLURGY"
        }
      ]
    },
    {
      "id": "T_METALLURGY",
      "name": "冶金技术",
      "desc": "将矿石冶炼成可用金属。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 35
        },
        {
          "id": "R_METAL_ORE",
          "need": 20
        },
        {
          "id": "R_COAL",
          "need": 15
        },
        {
          "id": "R_TOOLS",
          "need": 5
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_SMELTER"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_STEEL_MAKING"
        }
      ]
    },
    {
      "id": "T_STEEL_MAKING",
      "name": "炼钢技术",
      "desc": "生产高强度的钢材。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 45
        },
        {
          "id": "R_METAL",
          "need": 25
        },
        {
          "id": "R_COAL",
          "need": 30
        },
        {
          "id": "R_TOOLS",
          "need": 10
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_STEEL_MILL"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_MECHANIZATION"
        }
      ]
    },
    {
      "id": "T_MECHANIZATION",
      "name": "机械化",
      "desc": "用机器替代人力进行生产。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 60
        },
        {
          "id": "R_STEEL",
          "need": 20
        },
        {
          "id": "R_PARTS",
          "need": 15
        },
        {
          "id": "R_TOOLS",
          "need": 12
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_FACTORY"
        },
        {
          "type": "unlock",
          "target": "resource",
          "id": "R_MACHINERY"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_ELECTRIFICATION"
        }
      ]
    },
    {
      "id": "T_ELECTRIFICATION",
      "name": "电力技术",
      "desc": "掌握电能的生产和应用。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 75
        },
        {
          "id": "R_STEEL",
          "need": 35
        },
        {
          "id": "R_PARTS",
          "need": 25
        },
        {
          "id": "R_MACHINERY",
          "need": 8
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_POWER_PLANT"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_CHEMISTRY"
        }
      ]
    },
    {
      "id": "T_CHEMISTRY",
      "name": "化学工艺",
      "desc": "研究物质的化学性质和转化。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 85
        },
        {
          "id": "R_ELECTRICITY",
          "need": 80
        },
        {
          "id": "R_COAL",
          "need": 40
        },
        {
          "id": "R_PARTS",
          "need": 15
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_REFINERY"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_ELECTRONICS"
        }
      ]
    },
    {
      "id": "T_ELECTRONICS",
      "name": "电子技术",
      "desc": "制造电路和电子设备。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 100
        },
        {
          "id": "R_PLASTIC",
          "need": 25
        },
        {
          "id": "R_ELECTRICITY",
          "need": 150
        },
        {
          "id": "R_PARTS",
          "need": 20
        },
        {
          "id": "R_MACHINERY",
          "need": 10
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ELECTRONICS_PLANT"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_ADVANCED_COMPUTING"
        }
      ]
    },
    {
      "id": "T_ADVANCED_COMPUTING",
      "name": "高级计算",
      "desc": "开发强大的计算机系统。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 120
        },
        {
          "id": "R_CIRCUIT",
          "need": 40
        },
        {
          "id": "R_ELECTRICITY",
          "need": 250
        },
        {
          "id": "R_MACHINERY",
          "need": 15
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_TECH_CENTER"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_NUCLEAR_PHYSICS"
        }
      ]
    },
    {
      "id": "T_NUCLEAR_PHYSICS",
      "name": "核物理",
      "desc": "研究原子核的结构和能量。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 180
        },
        {
          "id": "R_ELECTRICITY",
          "need": 350
        },
        {
          "id": "R_CHIP",
          "need": 25
        },
        {
          "id": "R_MACHINERY",
          "need": 20
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_NUCLEAR_PLANT"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_ROCKETRY"
        }
      ]
    },
    {
      "id": "T_ROCKETRY",
      "name": "火箭技术",
      "desc": "开发进入太空的运载工具。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 250
        },
        {
          "id": "R_STEEL",
          "need": 60
        },
        {
          "id": "R_ROCKET_FUEL",
          "need": 60
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 150
        },
        {
          "id": "R_MACHINERY",
          "need": 25
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ROCKET_SILO"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_AEROSPACE_MATERIALS"
        }
      ]
    },
    {
      "id": "T_AEROSPACE_MATERIALS",
      "name": "航天材料",
      "desc": "开发轻量化高强度的航天材料。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 300
        },
        {
          "id": "R_STEEL",
          "need": 50
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 200
        },
        {
          "id": "R_CHIP",
          "need": 15
        },
        {
          "id": "R_MACHINERY",
          "need": 20
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ALLOY_WORKS"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_MICROELECTRONICS"
        }
      ]
    },
    {
      "id": "T_MICROELECTRONICS",
      "name": "微电子技术",
      "desc": "制造高精度微型芯片。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 350
        },
        {
          "id": "R_ALLOY",
          "need": 40
        },
        {
          "id": "R_CIRCUIT",
          "need": 60
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 300
        },
        {
          "id": "R_MACHINERY",
          "need": 25
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_CHIP_FAB"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_SPACE_STATIONS"
        }
      ]
    },
    {
      "id": "T_SPACE_STATIONS",
      "name": "空间站技术",
      "desc": "在轨道上建立永久居住点。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 450
        },
        {
          "id": "R_ALLOY",
          "need": 70
        },
        {
          "id": "R_CHIP",
          "need": 50
        },
        {
          "id": "R_ROCKET_FUEL",
          "need": 120
        },
        {
          "id": "R_LIFE_SUPPORT",
          "need": 30
        },
        {
          "id": "R_MACHINERY",
          "need": 30
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_SPACE_STATION"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_QUANTUM_MECHANICS"
        }
      ]
    },
    {
      "id": "T_QUANTUM_MECHANICS",
      "name": "量子力学",
      "desc": "探索微观世界的物理规律。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 700
        },
        {
          "id": "R_CHIP",
          "need": 70
        },
        {
          "id": "R_NUCLEAR_ENERGY",
          "need": 500
        },
        {
          "id": "R_ANTIMATTER",
          "need": 3
        },
        {
          "id": "R_MACHINERY",
          "need": 40
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_ANTIMATTER_LAB"
        },
        {
          "type": "unlock",
          "target": "research",
          "id": "T_INTERSTELLAR_TRAVEL"
        }
      ]
    },
    {
      "id": "T_INTERSTELLAR_TRAVEL",
      "name": "星际航行",
      "desc": "突破光速限制，进行星际旅行。",
      "defaultUnlock": false,
      "cost": [
        {
          "id": "R_KNOWLEDGE",
          "need": 1200
        },
        {
          "id": "R_ALLOY",
          "need": 120
        },
        {
          "id": "R_CHIP",
          "need": 100
        },
        {
          "id": "R_ANTIMATTER",
          "need": 15
        },
        {
          "id": "R_DARK_ENERGY",
          "need": 5
        },
        {
          "id": "R_MACHINERY",
          "need": 50
        }
      ],
      "prereqs": [],
      "effects": [
        {
          "type": "unlock",
          "target": "building",
          "id": "B_INTERSTELLAR_GATE"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_KNOWLEDGE",
          "count": 60,
          "per": "turn"
        }
      ]
    }
  ],
  "events":   [
    {
      "id": "E_COLD",
      "name": "寒冷",
      "desc": "气温骤降，需要更多燃料维持生存",
      "defaultUnlock": true,
      "weight": 10,
      "cooldown": 20,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_CAMPFIRE"
        }
      ],
      "effects": [
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_FOOD",
          "count": 30,
          "per": "occur"
        }
      ]
    },
    {
      "id": "E_BOUNTIFUL_HARVEST",
      "name": "丰收",
      "desc": "这一年风调雨顺，农作物产量大增",
      "defaultUnlock": false,
      "weight": 15,
      "cooldown": 30,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_FARMLAND"
        }
      ],
      "effects": [
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": 50,
          "per": "occur"
        }
      ]
    },
    {
      "id": "E_FOREST_FIRE",
      "name": "森林火灾",
      "desc": "一场大火烧毁了附近的森林",
      "defaultUnlock": false,
      "weight": 8,
      "cooldown": 40,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_LUMBER_CAMP"
        }
      ],
      "effects": [
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_WOOD",
          "count": 20,
          "per": "occur"
        }
      ]
    },
    {
      "id": "E_WOLF_ATTACK",
      "name": "狼群袭击",
      "desc": "饥饿的狼群袭击了营地",
      "defaultUnlock": true,
      "weight": 12,
      "cooldown": 25,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_CAMPFIRE"
        }
      ],
      "effects": [
        {
          "type": "randomProfessionLoss",
          "target": "profession",
          "id": "",
          "count": 1,
          "per": "occur"
        }
      ]
    },
    {
      "id": "E_MIGRANTS",
      "name": "移民抵达",
      "desc": "一群流浪者加入了你的聚落",
      "defaultUnlock": false,
      "weight": 10,
      "cooldown": 35,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_HUT"
        }
      ],
      "effects": [
        {
          "type": "add",
          "target": "profession",
          "id": "P_IDLE",
          "count": 2,
          "per": "occur"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": -20,
          "per": "occur"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_RATION",
          "count": 5,
          "per": "occur"
        }
      ]
    },
    {
      "id": "E_DISEASE",
      "name": "疾病爆发",
      "desc": "瘟疫在聚落中蔓延",
      "defaultUnlock": false,
      "weight": 8,
      "cooldown": 50,
      "prereqs": [
        {
          "type": "hasBuilding",
          "id": "B_HUT"
        }
      ],
      "effects": [
        {
          "type": "clamp",
          "target": "profession",
          "id": "P_IDLE",
          "count": 1,
          "per": "occur"
        },
        {
          "type": "add",
          "target": "resource",
          "id": "R_FOOD",
          "count": -25,
          "per": "occur"
        },
        {
          "type": "clamp",
          "target": "resource",
          "id": "R_RATION",
          "count": 8,
          "per": "occur"
        }
      ]
    }
  ],
};

const TARGET_NAME_CONVERT = {
  resource: "资源",
  building: "建筑",
  profession: "职业",
  research: "研究",
  event: "事件",
};

const PER_NAME_CONVERT = {
  turn: "每秒",
  occur: "每次发生",
  click: "每次点击",
};

const els = {
  resources: document.getElementById("resource-list"),
  buildings: document.getElementById("building-list"),
  events: document.getElementById("event-list"),
  professions: document.getElementById("profession-list"),
  researches: document.getElementById("research-list"),
  logs: document.getElementById("log-list"),
  versionBadge: document.getElementById("version-badge"),
  themeToggleButton: document.getElementById("theme-toggle-btn"),
  resetButton: document.getElementById("reset-save-btn"),
  tooltip: document.getElementById("tooltip"),
  status: document.getElementById("status-text"),
  calendar: document.getElementById("calendar-text"),
  toastStack: document.getElementById("toast-stack"),
};

let engine = null;
let currentState = null;
let previousResources = null;
let previousBuildings = null;
let previousResearches = null;
let previousEvents = null;
let showResourceDeltaFx = false;
const actionLogs = [];
const MAX_LOGS = 120;
const THEME_KEY = "dsr_theme";

function updateUiScale() {
  const widthScale = window.innerWidth / 1280;
  const heightScale = window.innerHeight / 760;
  const scale = Math.max(0.92, Math.min(1.35, Math.min(widthScale, heightScale)));
  document.documentElement.style.setProperty("--ui-scale", scale.toFixed(3));
}

function setStatus(text) {
  if (!els.status) return;
  els.status.textContent = text || "";
}

function setCalendar(year, day) {
  if (!els.calendar) return;
  els.calendar.textContent = `🗓️ 第 ${year} 年 · 第 ${day} 天`;
}

function applyTheme(theme) {
  const next = theme === "light" ? "light" : "dark";
  document.body.setAttribute("data-theme", next);
  if (els.themeToggleButton) {
    els.themeToggleButton.textContent = next === "light" ? "切换深色" : "切换浅色";
  }
}

function loadTheme() {
  const saved = localStorage.getItem(THEME_KEY) || "dark";
  applyTheme(saved);
}

function toggleTheme() {
  const current = document.body.getAttribute("data-theme") || "dark";
  const next = current === "dark" ? "light" : "dark";
  localStorage.setItem(THEME_KEY, next);
  applyTheme(next);
}

async function syncVersionFromPackage() {
  if (!els.versionBadge) return;
  try {
    const res = await fetch("./package.json", { cache: "no-store" });
    if (!res.ok) return;
    const pkg = await res.json();
    if (pkg && pkg.version) {
      els.versionBadge.textContent = `v${pkg.version}`;
    }
  } catch {
    // 静默失败，保留默认版本文案
  }
}

function fnum(value) {
  const n = Number(value ?? 0);
  const s = n.toFixed(3);
  return s.replace(/\.?0+$/, "");
}

function setTip(el, text) {
  el.dataset.tip = text || "";
}

function fitButtonText(btn, { max = 13, min = 9 } = {}) {
  if (!btn) return;

  // 先用最大字号，再按实际像素宽度逐步缩小
  let size = max;
  btn.style.fontSize = `calc(${size}px * var(--ui-scale))`;

  // 使用 scrollWidth/clientWidth 做真实宽度测量
  while (size > min && btn.scrollWidth > btn.clientWidth - 2) {
    size -= 0.5;
    btn.style.fontSize = `calc(${size}px * var(--ui-scale))`;
  }

  if (size < min) {
    btn.style.fontSize = `calc(${min}px * var(--ui-scale))`;
  }
}

function addLog(message) {
  const year = Number(currentState?.main?.year || 0);
  const day = Number(currentState?.main?.day || 0);
  const entry = {
    time: `${year}年${day}天`,
    message: message || "",
  };
  actionLogs.unshift(entry);
  if (actionLogs.length > MAX_LOGS) actionLogs.length = MAX_LOGS;

  if (!els.logs) return;
  els.logs.innerHTML = "";
  actionLogs.forEach((log) => {
    const row = document.createElement("div");
    row.className = "log-item";
    row.innerHTML = `<span class="log-time">[${log.time}]</span><span>${log.message}</span>`;
    els.logs.appendChild(row);
  });
}

function showToast(title, message, type = "info", ttl = 2400) {
  // 已停用右上角弹窗，统一改为日志输出
  const text = message ? `${title}：${message}` : title;
  addLog(text);
}

class LocalGameEngine {
  constructor(defs) {
    this.defs = defs;
    this.entityNames = new Map();
    this.resources = new Map();
    this.buildings = new Map();
    this.professions = new Map();
    this.researches = new Map();
    this.events = new Map();
    this.lastTickAt = Date.now();
    this.totalSimSeconds = 0;
    this.lastProcessedDay = 0;
    this.buildEntityNames();
    this.loadOrReset();
  }

  static create() {
    return new LocalGameEngine(EMBEDDED_DATA);
  }

  buildEntityNames() {
    const groups = [
      this.defs.resources,
      this.defs.buildings,
      this.defs.professions,
      this.defs.researches,
      this.defs.events,
    ];
    groups.forEach((list) => {
      list.forEach((item) => {
        this.entityNames.set(item.id, item.name);
      });
    });
  }

  loadOrReset() {
    const raw = localStorage.getItem(SAVE_KEY);
    if (!raw) {
      this.reset();
      return;
    }
    try {
      const snapshot = JSON.parse(raw);
      this.reset(false);
      this.restore(snapshot);
    } catch {
      this.reset();
    }
  }

  reset(save = true) {
    this.resources = new Map(
      this.defs.resources.map((def) => [
        def.id,
        {
          def,
          unlocked: !!def.defaultUnlock,
          amount: 0,
          capacity: Number(def.defaultCapacity || 0),
          rate: 0,
        },
      ]),
    );

    this.buildings = new Map(
      this.defs.buildings.map((def) => [
        def.id,
        {
          def,
          unlocked: !!def.defaultUnlock,
          ownedCount: 0,
        },
      ]),
    );

    this.professions = new Map(
      this.defs.professions.map((def) => [
        def.id,
        {
          def,
          unlocked: !!def.defaultUnlock,
          amount: 0,
          limit: 0,
        },
      ]),
    );

    this.researches = new Map(
      this.defs.researches.map((def) => [
        def.id,
        {
          def,
          unlocked: !!def.defaultUnlock,
          finished: false,
        },
      ]),
    );

    this.events = new Map(
      this.defs.events.map((def) => [
        def.id,
        {
          def,
          unlocked: !!def.defaultUnlock,
          activeUntilDay: 0,
          cooldownUntilDay: 0,
        },
      ]),
    );

    this.lastTickAt = Date.now();
    this.totalSimSeconds = 0;
    this.lastProcessedDay = 0;
    this.startGame();
    this.recomputeResourceRates();
    if (save) this.save();
  }

  restore(snapshot) {
    const restoreGroup = (map, patcher) => {
      if (!patcher || typeof patcher !== "object") return;
      Object.entries(patcher).forEach(([id, patch]) => {
        const state = map.get(id);
        if (!state || !patch || typeof patch !== "object") return;
        Object.assign(state, patch);
      });
    };

    restoreGroup(this.resources, snapshot.resources);
    restoreGroup(this.buildings, snapshot.buildings);
    restoreGroup(this.professions, snapshot.professions);
    restoreGroup(this.researches, snapshot.researches);
    restoreGroup(this.events, snapshot.events);

    this.lastTickAt = Number(snapshot.lastTickAt || Date.now());
    if (!Number.isFinite(this.lastTickAt)) {
      this.lastTickAt = Date.now();
    }
    this.totalSimSeconds = Number(snapshot.totalSimSeconds || 0);
    if (!Number.isFinite(this.totalSimSeconds) || this.totalSimSeconds < 0) {
      this.totalSimSeconds = 0;
    }
    this.lastProcessedDay = Number(snapshot.lastProcessedDay || Math.floor(this.totalSimSeconds / 60));
    if (!Number.isFinite(this.lastProcessedDay) || this.lastProcessedDay < 0) {
      this.lastProcessedDay = Math.floor(this.totalSimSeconds / 60);
    }
    this.recomputeResourceRates();
    this.save();
  }

  save() {
    const serialize = (map, fields) => {
      const out = {};
      map.forEach((state, id) => {
        out[id] = {};
        fields.forEach((key) => {
          out[id][key] = state[key];
        });
      });
      return out;
    };

    const snapshot = {
      resources: serialize(this.resources, ["unlocked", "amount", "capacity", "rate"]),
      buildings: serialize(this.buildings, ["unlocked", "ownedCount"]),
      professions: serialize(this.professions, ["unlocked", "amount", "limit"]),
      researches: serialize(this.researches, ["unlocked", "finished"]),
      events: serialize(this.events, ["unlocked", "activeUntilDay", "cooldownUntilDay"]),
      lastTickAt: this.lastTickAt,
      totalSimSeconds: this.totalSimSeconds,
      lastProcessedDay: this.lastProcessedDay,
    };
    localStorage.setItem(SAVE_KEY, JSON.stringify(snapshot));
  }

  startGame() {
    this.applyEffects([
      { type: "addLimit", target: "profession", id: "P_IDLE", count: 2 },
      { type: "add", target: "profession", id: "P_IDLE", count: 2, per: "click" },
    ]);
  }

  processEventDay(day) {
    let hasTriggered = false;
    this.events.forEach((state) => {
      if (!state.unlocked) return;

      // 冷却期内不进行判定
      if (day < (state.cooldownUntilDay || 0)) return;

      // 已触发高亮状态期间不重复触发
      if (day < (state.activeUntilDay || 0)) return;

      // 把原来的权重字段按“概率(%)”处理
      const probability = Math.max(0, Math.min(100, Number(state.def.weight || 0)));
      const roll = Math.random() * 100;
      if (roll < probability) {
        hasTriggered = true;
        // 触发后高亮1天
        state.activeUntilDay = day + 1;
        // 进入冷却（按“触发后 cd 天不可再次判定”）
        // 例如 cd=1，则下一天不可判定
        const cd = Math.max(0, Number(state.def.cooldown || 0));
        state.cooldownUntilDay = day + cd + 1;

        // 触发时立即执行一次性事件效果
        this.applyEffects(state.def.effects || []);
      }
    });

    if (hasTriggered) {
      this.recomputeResourceRates();
    }
  }

  processEventDays() {
    const currentDay = Math.floor(this.totalSimSeconds / 60);
    for (let day = this.lastProcessedDay + 1; day <= currentDay; day += 1) {
      this.processEventDay(day);
    }
    this.lastProcessedDay = currentDay;
  }

  tick() {
    const now = Date.now();
    const seconds = Math.floor((now - this.lastTickAt) / 1000);
    if (seconds <= 0) return false;
    this.lastTickAt += seconds * 1000;
    this.totalSimSeconds += seconds;

    this.resources.forEach((state) => {
      if (state.rate >= 0) {
        this.resourceAdd(state.def.id, state.rate, seconds);
      } else {
        this.resourceClamp(state.def.id, -state.rate, seconds);
      }
    });

    this.processEventDays();
    this.save();
    return true;
  }

  getEntityName(id) {
    return this.entityNames.get(id) || id;
  }

  getScaledCost(cost = [], ownedCount = 0) {
    const factor = Math.pow(1.2, Math.max(0, Number(ownedCount || 0)));
    return (cost || []).map((item) => ({
      id: item.id,
      need: Math.ceil(Number(item.need || 0) * factor),
    }));
  }

  getCostDesc(cost) {
    return `${this.getEntityName(cost.id)}: ${cost.need}`;
  }

  normalizeEffect(raw) {
    const effect = {
      type: raw?.type || "",
      target: raw?.target || "",
      toId: raw?.id || "",
      count: Number(raw?.count || 0),
      per: raw?.per || "",
      condition: raw?.condition || {},
      onlyOnce: raw?.per !== "turn",
      inTargets: raw?.inTargets || [],
      outTarget: raw?.outTarget || {},
      scope: raw?.scope || {},
      op: raw?.op || "",
      value: Number(raw?.value || 0),
    };
    if (effect.type === "addLimit" || effect.type === "unlock") {
      effect.onlyOnce = true;
    }
    return effect;
  }

  getOppositeEffect(effect) {
    if (effect.type === "add") {
      return {
        ...effect,
        type: "clamp",
      };
    }
    if (effect.type === "clamp") {
      return {
        ...effect,
        type: "add",
      };
    }
    return { ...effect };
  }

  effectDesc(raw) {
    const effect = this.normalizeEffect(raw);
    if (effect.type === "unlock") {
      return `解锁${TARGET_NAME_CONVERT[effect.target] || effect.target}: ${this.getEntityName(effect.toId)}`;
    }
    if (effect.type === "add") {
      return `${PER_NAME_CONVERT[effect.per] || ""}增加${this.getEntityName(effect.toId)}${TARGET_NAME_CONVERT[effect.target] || effect.target}: ${effect.count}`;
    }
    if (effect.type === "clamp") {
      return `${PER_NAME_CONVERT[effect.per] || ""}减少${this.getEntityName(effect.toId)}${TARGET_NAME_CONVERT[effect.target] || effect.target}: ${effect.count}`;
    }
    if (effect.type === "addLimit") {
      return `增加${this.getEntityName(effect.toId)}${TARGET_NAME_CONVERT[effect.target] || effect.target}上限: ${effect.count}`;
    }
    if (effect.type === "professionRateBuff") {
      return `提升职业 ${this.getEntityName(effect.toId)} 的资源增长速率: +${(effect.count * 100).toFixed(0)}%`;
    }
    if (effect.type === "randomProfessionLoss") {
      return `随机职业人数减少: ${effect.count}`;
    }
    if (effect.type === "convert") {
      return "转换作用";
    }
    return "无效果";
  }

  resourceAdd(resourceId, delta, timeDelta = 1) {
    const state = this.resources.get(resourceId);
    if (!state) return;
    state.amount = Math.min(state.capacity, state.amount + delta * timeDelta);
  }

  resourceClamp(resourceId, delta, timeDelta = 1) {
    const state = this.resources.get(resourceId);
    if (!state) return;
    state.amount = Math.max(0, state.amount - delta * timeDelta);
  }

  getProfessionRateMultiplier(professionId) {
    let mult = 1;
    this.researches.forEach((state) => {
      if (!state.unlocked || !state.finished) return;
      (state.def.effects || []).forEach((raw) => {
        const effect = this.normalizeEffect(raw);
        if (effect.type === "professionRateBuff" && effect.toId === professionId) {
          mult += effect.count;
        }
      });
    });
    return Math.max(0, mult);
  }

  recomputeResourceRates() {
    // 全量重算每回合资源速率，避免 +/- 人力分配导致的累计误差
    this.resources.forEach((state) => {
      state.rate = 0;
    });

    const applyTurnEffects = (effects = [], times = 1, addMultiplier = 1) => {
      (effects || []).forEach((raw) => {
        const effect = this.normalizeEffect(raw);
        if (effect.target !== "resource" || effect.per !== "turn") return;
        const resState = this.resources.get(effect.toId);
        if (!resState) return;

        if (effect.type === "add") {
          resState.rate += effect.count * times * addMultiplier;
        } else if (effect.type === "clamp") {
          resState.rate -= effect.count * times;
        }
      });
    };

    // 建筑：按拥有数量累加持续效果
    this.buildings.forEach((state) => {
      if (!state.unlocked || state.ownedCount <= 0) return;
      applyTurnEffects(state.def.effects || [], state.ownedCount);
    });

    // 研究：完成后持续效果生效
    this.researches.forEach((state) => {
      if (!state.unlocked || !state.finished) return;
      applyTurnEffects(state.def.effects || [], 1);
    });

    // 职业：按人数累加持续效果（可被科技加成）
    this.professions.forEach((state) => {
      if (!state.unlocked || state.amount <= 0) return;
      const profId = state.def.id;
      const mult = this.getProfessionRateMultiplier(profId);
      applyTurnEffects(state.def.effects || [], state.amount, mult);
    });
  }

  isEnough(cost = []) {
    return cost.every((item) => {
      const state = this.resources.get(item.id);
      return state && state.amount >= item.need;
    });
  }

  applyEffects(rawEffects) {
    const queue = (rawEffects || []).map((effect) => this.normalizeEffect(effect));
    while (queue.length > 0) {
      const effect = queue.shift();
      const extra = this.execEffect(effect);
      if (Array.isArray(extra) && extra.length > 0) {
        queue.push(...extra.map((item) => this.normalizeEffect(item)));
      }
    }
  }

  execEffect(effect) {
    switch (effect.target) {
      case "resource":
        return this.execResourceEffect(effect);
      case "building":
        return this.execBuildingEffect(effect);
      case "profession":
        return this.execProfessionEffect(effect);
      case "research":
        return this.execResearchEffect(effect);
      case "event":
        return this.execEventEffect(effect);
      default:
        return null;
    }
  }

  execResourceEffect(effect) {
    const state = this.resources.get(effect.toId);
    if (!state) return null;
    if (effect.type === "unlock") {
      state.unlocked = true;
      return null;
    }
    if (effect.type === "add") {
      if (effect.onlyOnce) {
        this.resourceAdd(effect.toId, effect.count);
      } else {
        state.rate += effect.count;
      }
      return null;
    }
    if (effect.type === "clamp") {
      if (effect.onlyOnce) {
        this.resourceClamp(effect.toId, effect.count);
      } else {
        state.rate -= effect.count;
      }
      return null;
    }
    if (effect.type === "addLimit") {
      state.capacity += effect.count;
    }
    return null;
  }

  execBuildingEffect(effect) {
    const state = this.buildings.get(effect.toId);
    if (!state) return null;
    if (effect.type === "unlock") {
      state.unlocked = true;
    }
    return null;
  }

  execProfessionEffect(effect) {
    if (effect.type === "randomProfessionLoss") {
      const lossCount = Math.max(1, Math.floor(effect.count || 1));
      const candidates = [];
      this.professions.forEach((profState, profId) => {
        if (!profState.unlocked || profState.amount <= 0) return;
        if (profId === "P_IDLE") return;
        candidates.push({ profId, profState });
      });
      if (candidates.length <= 0) return null;

      const pick = candidates[Math.floor(Math.random() * candidates.length)];
      const actualLoss = Math.min(lossCount, pick.profState.amount);
      pick.profState.amount -= actualLoss;

      const extras = [];
      for (let i = 0; i < actualLoss; i += 1) {
        (pick.profState.def.effects || []).forEach((raw) => {
          extras.push(this.getOppositeEffect(this.normalizeEffect(raw)));
        });
      }
      return extras;
    }

    const state = this.professions.get(effect.toId);
    if (!state) return null;

    if (effect.type === "unlock") {
      state.unlocked = true;
      return null;
    }

    if (effect.type === "add") {
      state.amount += effect.count;
      const extras = [];
      const repeats = Math.max(0, Math.floor(effect.count));
      for (let i = 0; i < repeats; i += 1) {
        extras.push(...(state.def.effects || []));
      }
      return extras;
    }

    if (effect.type === "clamp") {
      state.amount -= effect.count;
      const extras = [];
      const repeats = Math.max(0, Math.floor(effect.count));
      for (let i = 0; i < repeats; i += 1) {
        (state.def.effects || []).forEach((raw) => {
          extras.push(this.getOppositeEffect(this.normalizeEffect(raw)));
        });
      }
      return extras;
    }

    if (effect.type === "addLimit") {
      state.limit += effect.count;
    }

    return null;
  }

  execResearchEffect(effect) {
    const state = this.researches.get(effect.toId);
    if (!state) return null;
    if (effect.type === "unlock") {
      state.unlocked = true;
    }
    return null;
  }

  execEventEffect(effect) {
    const state = this.events.get(effect.toId);
    if (!state) return null;
    if (effect.type === "unlock") {
      state.unlocked = true;
    }
    return null;
  }

  build(buildingId) {
    this.tick();
    const state = this.buildings.get(buildingId);
    if (!state || !state.unlocked) return false;
    const cost = this.getScaledCost(state.def.cost || [], state.ownedCount);
    if (!this.isEnough(cost)) return false;

    cost.forEach((item) => {
      this.resourceClamp(item.id, item.need);
    });

    if (!state.def.onlyClick) {
      state.ownedCount += 1;
    }
    this.applyEffects(state.def.effects || []);
    this.recomputeResourceRates();
    this.save();
    return true;
  }

  research(researchId) {
    this.tick();
    const state = this.researches.get(researchId);
    if (!state || !state.unlocked || state.finished) return false;
    const cost = state.def.cost || [];
    if (!this.isEnough(cost)) return false;

    cost.forEach((item) => {
      this.resourceClamp(item.id, item.need);
    });

    state.finished = true;
    this.applyEffects(state.def.effects || []);
    this.recomputeResourceRates();
    this.save();
    return true;
  }

  canDispatch(fromProfessionId, toProfessionId) {
    const fromState = this.professions.get(fromProfessionId);
    const toState = this.professions.get(toProfessionId);
    if (!fromState || !toState || !toState.unlocked) return false;
    if (fromState.amount <= 0) return false;
    // 回收到闲置人口时不受上限限制，避免减员按钮失效
    if (toProfessionId !== "P_IDLE" && toState.amount >= toState.limit) return false;
    return true;
  }

  dispatch(fromProfessionId, toProfessionId) {
    this.tick();
    if (!this.canDispatch(fromProfessionId, toProfessionId)) return false;
    const fromState = this.professions.get(fromProfessionId);
    const toState = this.professions.get(toProfessionId);

    fromState.amount -= 1;
    toState.amount += 1;

    const effects = [];
    (fromState.def.effects || []).forEach((raw) => {
      effects.push(this.getOppositeEffect(this.normalizeEffect(raw)));
    });
    effects.push(...(toState.def.effects || []));
    this.applyEffects(effects);
    this.recomputeResourceRates();
    this.save();
    return true;
  }

  getRateBreakdown() {
    const byResource = {};

    const ensure = (resourceId) => {
      if (!byResource[resourceId]) {
        byResource[resourceId] = {
          byProfession: {},
          professionTotal: 0,
        };
      }
      return byResource[resourceId];
    };

    this.professions.forEach((profState) => {
      if (!profState.unlocked || profState.amount <= 0) return;
      const profId = profState.def.id;
      const mult = this.getProfessionRateMultiplier(profId);
      (profState.def.effects || []).forEach((raw) => {
        const effect = this.normalizeEffect(raw);
        if (effect.target !== "resource" || effect.per !== "turn") return;

        let delta = 0;
        if (effect.type === "add") {
          delta = effect.count * mult;
        } else if (effect.type === "clamp") {
          delta = -effect.count;
        }
        if (!delta) return;

        const bucket = ensure(effect.toId);
        const contrib = delta * profState.amount;
        bucket.byProfession[profId] = (bucket.byProfession[profId] || 0) + contrib;
        bucket.professionTotal += contrib;
      });

    });

    return byResource;
  }

  getFrontState() {
    this.tick();
    const rateBreakdown = this.getRateBreakdown();

    const resources = {};
    this.resources.forEach((state, id) => {
      if (!state.unlocked) return;
      const bucket = rateBreakdown[id] || { byProfession: {}, professionTotal: 0 };
      resources[id] = {
        id,
        name: state.def.name,
        desc: state.def.desc,
        count: state.amount,
        limit: state.capacity,
        rate: state.rate,
        rateBreakdown: {
          byProfession: bucket.byProfession,
          professionTotal: bucket.professionTotal,
          other: state.rate - bucket.professionTotal,
        },
      };
    });

    const buildings = {};
    this.buildings.forEach((state, id) => {
      if (!state.unlocked) return;
      const cost = this.getScaledCost(state.def.cost || [], state.ownedCount);
      buildings[id] = {
        id,
        name: state.def.name,
        desc: state.def.desc,
        cost,
        count: state.ownedCount,
        canBuild: this.isEnough(cost),
        costDesc: cost.map((item) => this.getCostDesc(item)),
        effectsDesc: (state.def.effects || []).map((effect) => this.effectDesc(effect)),
      };
    });

    const professions = {};
    this.professions.forEach((state, id) => {
      if (!state.unlocked) return;
      professions[id] = {
        id,
        name: state.def.name,
        desc: state.def.desc,
        count: state.amount,
        limit: state.limit,
        canEdit: !!state.def.editable,
        effectsDesc: (state.def.effects || []).map((effect) => this.effectDesc(effect)),
      };
    });

    const research = {};
    this.researches.forEach((state, id) => {
      if (!state.unlocked) return;
      const cost = state.def.cost || [];
      research[id] = {
        id,
        name: state.def.name,
        desc: state.def.desc,
        cost,
        finished: !!state.finished,
        unlocked: !!state.unlocked,
        canResearch: !state.finished && this.isEnough(cost),
        costDesc: cost.map((item) => this.getCostDesc(item)),
        effectsDesc: (state.def.effects || []).map((effect) => this.effectDesc(effect)),
      };
    });

    const events = {};
    const currentDay = Math.floor(this.totalSimSeconds / 60);
    this.events.forEach((state, id) => {
      if (!state.unlocked) return;
      const probability = Number(state.def.weight || 0);
      const cooldown = Number(state.def.cooldown || 0);
      const isActive = currentDay < (state.activeUntilDay || 0);
      const cooldownRemaining = Math.max(0, (state.cooldownUntilDay || 0) - currentDay);
      events[id] = {
        id,
        name: state.def.name,
        desc: state.def.desc,
        probability,
        cooldown,
        cooldownRemaining,
        isActive,
        prereqs: state.def.prereqs || [],
        effects: (state.def.effects || []).map((effect) => this.effectDesc(effect)),
      };
    });

    const totalDays = Math.floor(this.totalSimSeconds / 60);
    const year = Math.floor(totalDays / 365);
    const day = totalDays % 365;

    return {
      main: {
        totalSimSeconds: this.totalSimSeconds,
        totalDays,
        year,
        day,
      },
      resources,
      buildings,
      professions,
      research,
      events,
    };
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

function refreshState() {
  if (!engine) return;

  if (currentState) {
    previousResources = currentState.resources ? Object.values(currentState.resources) : null;
    previousBuildings = currentState.buildings ? Object.values(currentState.buildings) : null;
    previousResearches = currentState.research ? Object.values(currentState.research) : null;
    previousEvents = currentState.events ? Object.values(currentState.events) : null;
  }

  currentState = engine.getFrontState();
  render(currentState || {});
  const year = Number(currentState?.main?.year || 0);
  const day = Number(currentState?.main?.day || 0);
  setCalendar(year, day);
}

function formatRateBreakdown(resource) {
  const rb = resource.rateBreakdown;
  if (!rb) return "";

  const profMap = (currentState && currentState.professions) ? currentState.professions : {};
  const lines = [];

  Object.entries(rb.byProfession || {}).forEach(([profId, value]) => {
    if (Math.abs(value) < 0.001) return;
    const profName = profMap[profId]?.name || profId;
    lines.push(`${value >= 0 ? "+" : ""}${value.toFixed(2)} ${profName}`);
  });

  if (Math.abs(rb.other || 0) >= 0.001) {
    lines.push(`${rb.other >= 0 ? "+" : ""}${rb.other.toFixed(2)} 其他来源(建筑/研究/事件)`);
  }

  if (lines.length === 0) return "";
  return `\n\n【速率来源】\n${lines.join("\n")}`;
}

function renderResources(resources) {
  els.resources.innerHTML = "";
  resources.forEach((r) => {
    const row = document.createElement("div");
    row.className = "resource-item";
    row.dataset.resourceId = r.id;
    const rate = Number(r.rate || 0);
    const rateClass = rate > 0 ? "pos" : rate < 0 ? "neg" : "zero";
    row.innerHTML = `<span>${r.name} ${fnum(r.count)}/${fnum(r.limit)}</span>
      <span class="resource-rate ${rateClass}">${rate >= 0 ? "+" : ""}${rate.toFixed(2)}</span>`;
    const breakdownText = formatRateBreakdown(r);
    setTip(row, `【资源】${r.name}\n${r.desc || ""}${breakdownText}`);
    els.resources.appendChild(row);
  });
}

function renderBuildings(buildings, nameOf, dontChangeButtonStatus = false) {
  const exist = els.buildings.querySelectorAll("[data-building-id]");
  const existMap = new Map();
  exist.forEach((node) => {
    existMap.set(node.dataset.buildingId, node);
  });
  const seen = new Set();

  buildings.forEach((b) => {
    let btn = existMap.get(b.id);
    const isNew = !btn;
    if (!btn) {
      btn = document.createElement("button");
      btn.className = "btn";
      btn.dataset.buildingId = b.id;
    }

    if (!dontChangeButtonStatus) {
      btn.disabled = !b.canBuild;
    }

    const nextText = b.count > 0 ? `${b.name}(${b.count})` : b.name;
    if (btn.textContent !== nextText) {
      btn.textContent = nextText;
    }
    // 建筑按钮动态字体，避免文字长度挤压 UI
    fitButtonText(btn, { max: 13, min: 9 });

    if (isNew) {
      btn.addEventListener("click", () => {
        const ok = engine.build(btn.dataset.buildingId);
        if (!ok) {
          showToast("无法建造", "资源不足或尚未解锁", "warn");
          refreshState();
          return;
        }
        showResourceDeltaFx = true;
        refreshState();
      });
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
    label.classList.toggle("active-event", !!ev.isActive);
    const effects = (ev.effects || []).join("\n");
    let tip = `【事件】${ev.name}\n${ev.desc || ""}\n`;
    if (typeof ev.probability !== "undefined") {
      tip += `\n【触发概率】${ev.probability}%`;
    }
    if (typeof ev.cooldown !== "undefined") {
      tip += `\n【冷却(天)】${ev.cooldown}`;
    }
    if (typeof ev.cooldownRemaining !== "undefined") {
      tip += `\n【剩余冷却】${ev.cooldownRemaining}天`;
    }
    if (ev.isActive) {
      tip += `\n【状态】已触发（本天高亮）`;
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
      add.addEventListener("click", () => {
        const ok = engine.dispatch("P_IDLE", p.id);
        if (!ok) {
          showToast("无法分配", "闲置人口不足或职业已满", "warn");
        } else {
          addLog(`职业变动：闲置 -> ${p.name}`);
        }
        refreshState();
      });
      ops.appendChild(add);

      const sub = document.createElement("button");
      sub.className = "op-btn";
      sub.textContent = "-";
      const canSub = p.count > 0;
      sub.disabled = !canSub;
      sub.addEventListener("click", () => {
        const ok = engine.dispatch(p.id, "P_IDLE");
        if (!ok) {
          showToast("无法撤回", "没有可撤回的人力", "warn");
        } else {
          addLog(`职业变动：${p.name} -> 闲置`);
        }
        refreshState();
      });
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
  const exist = els.researches.querySelectorAll("[data-research-id]");
  const existMap = new Map();
  exist.forEach((node) => {
    existMap.set(node.dataset.researchId, node);
  });
  const seen = new Set();

  researches.forEach((r) => {
    let btn = existMap.get(r.id);
    const isNew = !btn;
    if (!btn) {
      btn = document.createElement("button");
      btn.className = "btn research-btn";
      btn.dataset.researchId = r.id;
    }

    const nextText = r.finished ? `${r.name}(已完成)` : r.name;
    if (btn.textContent !== nextText) {
      btn.textContent = nextText;
    }

    btn.classList.toggle("completed", !!r.finished);
    // 研究按钮预留完成态空间，完成后略微缩小字体
    fitButtonText(btn, r.finished ? { max: 10, min: 8 } : { max: 11, min: 9 });

    if (!dontChangeButtonStatus) {
      btn.disabled = !!r.finished || r.canResearch === false;
    }

    if (isNew) {
      btn.addEventListener("click", () => {
        const ok = engine.research(btn.dataset.researchId);
        if (!ok) {
          showToast("无法研究", "资源不足、未解锁或已完成", "warn");
          refreshState();
          return;
        }
        showResourceDeltaFx = true;
        refreshState();
      });
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
  renderBuildings(buildings, nameOf, false);
  renderEvents(events);
  renderProfessions(professions);
  renderResearches(researches, nameOf, false);

  requestAnimationFrame(() => {
    if (showResourceDeltaFx) {
      const resourceChanges = detectResourceChanges(resources, previousResources);
      (resourceChanges || []).forEach((change) => {
        const resourceEl = document.querySelector(`[data-resource-id="${change.id}"]`);
        if (!resourceEl) return;
        const rect = resourceEl.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top;
        const sign = change.isPositive ? "+" : "";
        showFloatingNumber(x, y, `${sign}${change.diff.toFixed(1)} ${change.name}`, change.isPositive);
      });
      showResourceDeltaFx = false;
    }

    const newBuildings = detectNewBuildings(buildings, previousBuildings);
    (newBuildings || []).forEach((b) => {
      const btn = document.querySelector(`[data-building-id="${b.id}"]`);
      if (!btn) return;
      triggerPulseAnimation(btn);
      addLog(`建造完成：${b.name}`);
    });

    const newResearches = detectNewResearches(researches, previousResearches);
    (newResearches || []).forEach((r) => {
      addLog(`研究完成：${r.name}`);
      showFullscreenNotify("研究完成！", `${r.name} - ${r.desc || "新技术已解锁"}`, "🔬");
    });

    const newActiveEvents = detectNewActiveEvents(events, previousEvents);
    (newActiveEvents || []).forEach((ev) => {
      const effectText = (ev.effects && ev.effects.length > 0) ? ev.effects.join("；") : "无";
      addLog(`事件触发：${ev.name}｜影响：${effectText}`);
    });
  });
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

function showFloatingNumber(x, y, text, isPositive) {
  const el = document.createElement("div");
  el.className = `floating-number ${isPositive ? "positive" : "negative"}`;
  el.textContent = text;
  el.style.left = `${x}px`;
  el.style.top = `${y}px`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1200);
}

function showFullscreenNotify(title, desc, icon = "[]") {
  const overlay = document.createElement("div");
  overlay.className = "fullscreen-notify";
  overlay.innerHTML = `
    <div class="fullscreen-notify-content">
      <div class="fullscreen-notify-icon">${icon}</div>
      <div class="fullscreen-notify-title">${title}</div>
      <div class="fullscreen-notify-desc">${desc}</div>
    </div>
  `;
  document.body.appendChild(overlay);

  const close = () => {
    overlay.classList.add("closing");
    setTimeout(() => overlay.remove(), 300);
  };

  overlay.addEventListener("click", close);
  setTimeout(close, 3500);
}

function triggerPulseAnimation(element) {
  if (!element) return;
  element.classList.remove("pulse-animation");
  element.classList.remove("flash-animation");
  void element.offsetWidth;
  element.classList.add("pulse-animation");
  element.classList.add("flash-animation");
  setTimeout(() => {
    element.classList.remove("pulse-animation");
    element.classList.remove("flash-animation");
  }, 1000);
}

function detectResourceChanges(current, previous) {
  if (!previous) return [];
  const changes = [];
  current.forEach((r) => {
    const prev = previous.find((p) => p.id === r.id);
    if (!prev) return;
    const diff = (r.count || 0) - (prev.count || 0);
    if (Math.abs(diff) > 0.01) {
      changes.push({
        id: r.id,
        name: r.name,
        diff,
        isPositive: diff > 0,
      });
    }
  });
  return changes;
}

function detectNewBuildings(current, previous) {
  if (!previous) return [];
  return current.filter((b) => {
    const prev = previous.find((p) => p.id === b.id);
    return prev && b.count > prev.count;
  });
}

function detectNewResearches(current, previous) {
  if (!previous) return [];
  return current.filter((r) => {
    const prev = previous.find((p) => p.id === r.id);
    return prev && r.finished && !prev.finished;
  });
}

function detectNewActiveEvents(current, previous) {
  if (!previous) return [];
  return current.filter((ev) => {
    const prev = previous.find((p) => p.id === ev.id);
    return prev && ev.isActive && !prev.isActive;
  });
}

async function boot() {
  updateUiScale();
  window.addEventListener("resize", updateUiScale);
  bindTooltip();
  loadTheme();
  syncVersionFromPackage();
  if (els.themeToggleButton) {
    els.themeToggleButton.addEventListener("click", () => {
      toggleTheme();
    });
  }
  if (els.resetButton) {
    els.resetButton.addEventListener("click", () => {
      if (!engine) return;
      engine.reset();
      previousResources = null;
      previousBuildings = null;
      previousResearches = null;
      previousEvents = null;
      actionLogs.length = 0;
      refreshState();
      addLog("存档已重置，重新开始");
    });
  }

  try {
    engine = await LocalGameEngine.create();
    refreshState();
    addLog("系统初始化完成");
    setInterval(() => refreshState(), 1000);
  } catch (err) {
    const msg = String(err);
    if (location.protocol === "file:") {
      setStatus("初始化失败 | 请通过本地静态服务器打开 game.html");
    } else {
      setStatus(`初始化失败: ${msg}`);
    }
    showToast("初始化失败", msg, "error", 5000);
  }
}

boot();
