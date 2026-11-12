```cardspec
{
  "title": "电池状态",
  "description": "电量与充电状态速览",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"手机电量","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"title_icon","component":"Image","src":"resources/base/media/bolt_fill.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF1F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"状态","styles":{"height":14,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/phoneBattery/chargingStatusDesc} }}","styles":{"height":14.0,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":14.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":14.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"phoneBattery":{"batterySOCText":"68%","chargingStatusDesc":"未充电"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张手机电池电量卡片，显示当前电量百分比和充电状态，当手机充满电时播报充电完成。",
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
      "id": "asset.bolt_fill",
      "src": "resources/base/media/bolt_fill.svg",
      "description": "样式：默认黑色的单色实心竖向闪电图标；适用：正在充电、快充、电能或闪电状态。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetPhoneBatteryInfo"
  ],
  "event": [],
  "asset": [
    "asset.bolt_fill"
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
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.bolt_fill"
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
  "artifactId": "6db38fc2-3efb-40d1-aee6-6a871321773b",
  "createdAt": 1793951082410
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":"手机电量","icon":"resources/base/media/bolt_fill.svg","fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/phoneBattery/batterySOCText"},"fontSize":30}]
["support","SecondaryBody",{"items":[{"label":"状态","value":{"path":"/data/phoneBattery/chargingStatusDesc"}}],"fontSize":14}]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/chargingStatusDesc","未充电"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL00 7.0.0.111",
    "candidateAssetIds": [
      "asset.bolt_fill"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "电量与充电状态速览",
    "userQuery": "做一张手机电池电量卡片，显示当前电量百分比和充电状态，当手机充满电时播报充电完成。",
    "title": "电池状态",
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
    "phoneType": "CMM-AL00",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101100001716"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q435-000",
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
  "romVersion": "CMM-AL00 7.0.0.111",
  "candidateAssetIds": [
    "asset.bolt_fill"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "电量与充电状态速览",
  "userQuery": "做一张手机电池电量卡片，显示当前电量百分比和充电状态，当手机充满电时播报充电完成。",
  "title": "电池状态",
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
