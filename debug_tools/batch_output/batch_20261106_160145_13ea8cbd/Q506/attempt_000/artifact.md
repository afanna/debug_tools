```cardspec
{
  "title": "电量管理",
  "description": "查看电量，一键省电",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["fusionBallBackground","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#00000000"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F9985","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF24B3B3","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF5AB38E","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"手机电量","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#CCFFFFFF"}},{"id":"title_icon","component":"Image","src":"resources/base/media/battery_leaf_fill.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FFFFFFFF"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary_support","__layout__root__action"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary_support","component":"Column","children":["primary","support"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"primary","component":"Row","children":["primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"support","component":"Column","children":["support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"状态","styles":{"height":14,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/phoneBattery/chargingStatusDesc} }}","styles":{"height":14.0,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FFFFFFFF","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":14.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":14.0,"alignItems":"top","flexShrink":0}},{"id":"__layout__root__action","component":"Column","children":["action"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","height":36,"flexShrink":0},"itemMargin":0},{"id":"action","component":"Row","children":["action_icon","action_text"],"onClick":[{"call":"clickToIntent","args":{"intentName":"SetSettingSwitch","params":{"appBundleName":"com.huawei.hmos.settings","itemName":"battery_saving_mode"}}}],"itemMargin":8,"styles":{"height":36,"borderRadius":30,"padding":0,"flexShrink":0,"width":"matchParent","backgroundColor":"#33FFFFFF","justifyContent":"center","alignItems":"center"}},{"id":"action_icon","component":"Image","src":"resources/base/media/ic_switch.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FFFFFFFF"}},{"id":"action_text","component":"Text","content":"开启省电","styles":{"maxWidth":96,"height":17,"fontSize":14,"fontWeight":500,"textAlign":"center","maxLines":1,"flexShrink":0,"fontColor":"#FFFFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"phoneBattery":{"batterySOCText":"68%","chargingStatusDesc":"未充电"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一个手机电量管理卡片，能查看当前电量，还能一键开启省电模式",
  "size": "2x2",
  "appVersion": "11.7.8.392",
  "eventCandidates": [
    {
      "id": "event.setPowerSavingMode",
      "description": "点击操作省电模式开关。",
      "call": "clickToIntent",
      "args": {
        "intentName": "SetSettingSwitch",
        "params": {
          "appBundleName": "com.huawei.hmos.settings",
          "itemName": "battery_saving_mode"
        }
      }
    }
  ],
  "dataModelSchema": {
    "data": {
      "phoneBattery": {
        "batterySOCText": {
          "type": "string",
          "description": "可直接显示的当前手机设备剩余电量文本，已包含“%”单位；展示时不得再次追加“%”。",
          "sampleValue": "68%",
          "numericSource": "/data/phoneBattery/batterySOC"
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "当前设备电池的充电状态文本描述。",
          "sampleValue": "未充电"
        },
        "batterySOC": {
          "type": "integer",
          "description": "当前手机设备剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”；优先使用 batterySOCText。",
          "sampleValue": 68
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.battery_leaf_fill",
      "src": "resources/base/media/battery_leaf_fill.svg",
      "description": "样式：默认黑色的单色实心横向电池图标，电池内部为叶片留白；适用：电池相关场景，包括电量、省电模式、节能电池、绿色用电状态，也可作为电池健康或电池温度信息的辅助图标，相关数据可结合 GetPhoneBatteryInfo 展示。图标本身不表示具体电量、健康等级或温度高低。"
    },
    {
      "id": "asset.ic_switch",
      "src": "resources/base/media/ic_switch.svg",
      "description": "样式：默认黑色的单色双滑块开关图标，两个水平开关轨道分别朝向相反位置，原始尺寸为 96×96；适用：系统设置类开关控制卡片，可配合 event.setBluetoothMode 等设置开关事件表达开启或关闭操作。图标本身不表示具体开关当前状态，实际状态以对应数据能力支持为准。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetPhoneBatteryInfo"
  ],
  "event": [
    {
      "id": "event.setPowerSavingMode",
      "description": "点击操作省电模式开关。",
      "call": "clickToIntent",
      "args": {
        "intentName": "SetSettingSwitch",
        "params": {
          "appBundleName": "com.huawei.hmos.settings",
          "itemName": "battery_saving_mode"
        }
      }
    }
  ],
  "asset": [
    "asset.battery_leaf_fill",
    "asset.ic_switch"
  ]
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.setPowerSavingMode",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "SetSettingSwitch",
          "params": {
            "appBundleName": "com.huawei.hmos.settings",
            "itemName": "battery_saving_mode"
          }
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.battery_leaf_fill",
    "asset.ic_switch"
  ]
}
```
```meta
{
  "apiVersion": "v1",
  "taskSpecVersion": "task-spec-v1",
  "cardSpecVersion": "card-spec-v1",
  "dslProtocolVersion": "v0.9",
  "skillVersion": "skill-widget-v1",
  "protocolProfileId": "a2ui-form-rom6.0-v1",
  "capabilityRegistryVersion": "app-11.7.7.300_rom-7.0",
  "artifactSchemaVersion": "widget-artifact-v2",
  "generationMode": "create",
  "artifactId": "99ec4589-5241-4ac3-a75b-d80ed196aea8",
  "createdAt": 1793952348854
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-primary-secondary-action"},["title","primary","support","action"]]
["title","SingleLineTitle",{"title":"手机电量","icon":"resources/base/media/battery_leaf_fill.svg","fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/phoneBattery/batterySOCText"},"fontSize":30}]
["support","SecondaryBody",{"items":[{"label":"状态 ","value":{"path":"/data/phoneBattery/chargingStatusDesc"}}],"fontSize":14}]
["action","PillButton",{"label":"开启省电","icon":"resources/base/media/ic_switch.svg","onClick":[{"call":"clickToIntent","args":{"intentName":"SetSettingSwitch","params":{"appBundleName":"com.huawei.hmos.settings","itemName":"battery_saving_mode"}}}]}]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/chargingStatusDesc","未充电"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CLS-AL00 7.0.0.111",
    "candidateAssetIds": [
      "asset.battery_leaf_fill",
      "asset.ic_switch"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.setPowerSavingMode",
        "action": {
          "call": "clickToIntent",
          "args": {
            "intentName": "SetSettingSwitch",
            "params": {
              "appBundleName": "com.huawei.hmos.settings",
              "itemName": "battery_saving_mode"
            }
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "查看电量，一键省电",
    "userQuery": "创建一个手机电量管理卡片，能查看当前电量，还能一键开启省电模式",
    "title": "电量管理",
    "candidateDataBindings": [
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/phoneBattery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc",
          "/batterySOC"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CLS-AL00",
    "prdVer": "11.7.8.392",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261106011202258"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q506-000",
    "isNew": true,
    "sessionId": "batch-13ea8cbd"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "size": "2x2",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CLS-AL00 7.0.0.111",
  "candidateAssetIds": [
    "asset.battery_leaf_fill",
    "asset.ic_switch"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.setPowerSavingMode",
      "action": {
        "call": "clickToIntent",
        "args": {
          "intentName": "SetSettingSwitch",
          "params": {
            "appBundleName": "com.huawei.hmos.settings",
            "itemName": "battery_saving_mode"
          }
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "查看电量，一键省电",
  "userQuery": "创建一个手机电量管理卡片，能查看当前电量，还能一键开启省电模式",
  "title": "电量管理",
  "candidateDataBindings": [
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    }
  ]
}
```
