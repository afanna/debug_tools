```cardspec
{
  "title": "电池状态",
  "description": "电池信息速览",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"电池状态","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0","support_row1","support_row2","support_row3"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"充电状态","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/phoneBattery/chargingStatusDesc} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item1_label","component":"Text","content":"温度","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item1_value","component":"Text","content":"{{ ${/data/phoneBattery/batteryTemperatureText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item1","component":"Row","children":["support_item1_label","support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row1","component":"Row","children":["support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item2_label","component":"Text","content":"电流","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item2_value","component":"Text","content":"{{ ${/data/phoneBattery/nowCurrentText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item2","component":"Row","children":["support_item2_label","support_item2_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row2","component":"Row","children":["support_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item3_label","component":"Text","content":"电压","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item3_value","component":"Text","content":"{{ ${/data/phoneBattery/voltageText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item3","component":"Row","children":["support_item3_label","support_item3_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row3","component":"Row","children":["support_item3"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"phoneBattery":{"batterySOCText":"68%","chargingStatusDesc":"未充电","batteryTemperatureText":"29.0 ℃","nowCurrentText":"-151 mA","voltageText":"4 V"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张电池状态卡片，显示当前电量、充电状态、电池温度、电流、电压等电池信息。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
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
        "batteryTemperatureText": {
          "type": "string",
          "description": "可直接显示的当前设备电池实时温度文本，已包含“℃”单位；展示时不得再次追加温度单位。",
          "sampleValue": "29.0 ℃"
        },
        "nowCurrentText": {
          "type": "string",
          "description": "可直接显示的当前设备电池实时电流文本，已包含“mA”单位；展示时不得再次追加电流单位。",
          "sampleValue": "-151 mA"
        },
        "voltageText": {
          "type": "string",
          "description": "可直接显示的当前设备电池实时电压文本，已包含“V”单位；展示时不得再次追加电压单位。",
          "sampleValue": "4 V"
        },
        "batterySOC": {
          "type": "integer",
          "description": "当前手机设备剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”；优先使用 batterySOCText。",
          "sampleValue": 68
        }
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "GetPhoneBatteryInfo"
  ],
  "event": [],
  "asset": []
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
        "/batteryTemperatureText",
        "/nowCurrentText",
        "/voltageText",
        "/batterySOC"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": []
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
  "artifactId": "cfc2ee2c-7149-43e4-af4a-055d023657d2",
  "createdAt": 1793934591980
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":"电池状态","fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/phoneBattery/batterySOCText"},"fontSize":30}]
["support","SecondaryBody",{"columns":1,"items":[{"label":"充电状态","value":{"path":"/data/phoneBattery/chargingStatusDesc"}},{"label":"温度","value":{"path":"/data/phoneBattery/batteryTemperatureText"}},{"label":"电流","value":{"path":"/data/phoneBattery/nowCurrentText"}},{"label":"电压","value":{"path":"/data/phoneBattery/voltageText"}}],"fontSize":12}]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/chargingStatusDesc","未充电"]
["/data/phoneBattery/batteryTemperatureText","29.0 ℃"]
["/data/phoneBattery/nowCurrentText","-151 mA"]
["/data/phoneBattery/voltageText","4 V"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一张电池状态卡片，显示当前电量、充电状态、电池温度、电流、电压等电池信息。",
    "candidateDataBindings": [
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/phoneBattery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc",
          "/batteryTemperatureText",
          "/nowCurrentText",
          "/voltageText",
          "/batterySOC"
        ]
      }
    ],
    "title": "电池状态",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "电池信息速览",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMU-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261030130425457"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q358-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一张电池状态卡片，显示当前电量、充电状态、电池温度、电流、电压等电池信息。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMU-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一张电池状态卡片，显示当前电量、充电状态、电池温度、电流、电压等电池信息。",
  "candidateDataBindings": [
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batteryTemperatureText",
        "/nowCurrentText",
        "/voltageText",
        "/batterySOC"
      ]
    }
  ],
  "title": "电池状态",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "电池信息速览",
  "candidateAssetIds": []
}
```
