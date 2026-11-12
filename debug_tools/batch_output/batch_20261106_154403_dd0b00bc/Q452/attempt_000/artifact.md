```cardspec
{
  "title": "当前电量",
  "description": "手机电量速览",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["fusionBallBackground","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#00000000"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F9985","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF24B3B3","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF5AB38E","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["content"],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"center","padding":12},"itemMargin":0},{"id":"content","component":"Column","children":["content_label","content_value","content_supporting"],"itemMargin":8,"styles":{"width":"matchParent","height":114,"alignItems":"center","justifyContent":"center","flexShrink":1}},{"id":"content_label","component":"Text","content":"手机电量","styles":{"width":"matchParent","height":18,"fontSize":12,"fontWeight":500,"textAlign":"center","maxLines":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"content_value","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"height":60,"fontSize":48,"fontWeight":700,"textAlign":"center","maxLines":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"content_supporting","component":"Text","content":"{{ ${/data/phoneBattery/batteryCapacityLevelDesc} }}","styles":{"height":20,"fontSize":14,"fontWeight":400,"textAlign":"center","maxLines":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"phoneBattery":{"batterySOCText":"68%","batteryCapacityLevelDesc":"正常电量"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张低电量卡片，显示当前手机电量",
  "size": "2x2",
  "appVersion": "11.7.9.300",
  "eventCandidates": [
    {
      "id": "event.open.settings.battery",
      "description": "打开华为手机自带的系统设置中的电池页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.settings.MainAbility",
        "bundleName": "com.huawei.hmos.settings",
        "intentName": "Settings",
        "uri": "battery"
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
        "batteryCapacityLevelDesc": {
          "type": "string",
          "description": "设备电池电量等级的语义化文本描述。",
          "sampleValue": "正常电量"
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
      "id": "event.open.settings.battery",
      "description": "打开华为手机自带的系统设置中的电池页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "com.huawei.hmos.settings.MainAbility",
        "bundleName": "com.huawei.hmos.settings",
        "intentName": "Settings",
        "uri": "battery"
      }
    }
  ],
  "asset": [
    "asset.battery_leaf_fill"
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
        "/batteryCapacityLevelDesc",
        "/batterySOC"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.settings.battery",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.settings.MainAbility",
          "bundleName": "com.huawei.hmos.settings",
          "intentName": "Settings",
          "uri": "battery"
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.battery_leaf_fill"
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
  "artifactId": "afd8ff69-641d-4aa2-9266-c02225aa4bc8",
  "createdAt": 1793951117817
}
```
```designcompactdsl
["root","Layout",{"layout":"S-center"},["content"]]
["content","DataDisplay",{"label":"手机电量","value":{"path":"/data/phoneBattery/batterySOCText"},"supportingText":{"path":"/data/phoneBattery/batteryCapacityLevelDesc"}}]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/batteryCapacityLevelDesc","正常电量"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.120",
    "candidateAssetIds": [
      "asset.battery_leaf_fill"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.settings.battery",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "com.huawei.hmos.settings.MainAbility",
            "bundleName": "com.huawei.hmos.settings",
            "intentName": "Settings",
            "uri": "battery"
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "手机电量速览",
    "userQuery": "创建一张低电量卡片，显示当前手机电量",
    "title": "当前电量",
    "candidateDataBindings": [
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/phoneBattery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc",
          "/batteryCapacityLevelDesc",
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
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.9.300",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261104072513371"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q452-000",
    "isNew": true,
    "sessionId": "batch-dd0b00bc"
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
  "romVersion": "CMS-AL20 7.0.0.120",
  "candidateAssetIds": [
    "asset.battery_leaf_fill"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.settings.battery",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "com.huawei.hmos.settings.MainAbility",
          "bundleName": "com.huawei.hmos.settings",
          "intentName": "Settings",
          "uri": "battery"
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "手机电量速览",
  "userQuery": "创建一张低电量卡片，显示当前手机电量",
  "title": "当前电量",
  "candidateDataBindings": [
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batteryCapacityLevelDesc",
        "/batterySOC"
      ]
    }
  ]
}
```
