```cardspec
{
  "title": "耳机状态",
  "description": "连接与电量速览",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/earphone/earphoneName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"title_icon","component":"Image","src":"resources/base/media/emoji_bluetooth_earbuds_black.png","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["status"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"status","component":"Column","children":["status_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"status_main","component":"Text","content":"{{ ${/data/earphone/isConnected} ? '已连接' : '未连接' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details","component":"Column","children":["details_row0","details_row1","details_row2"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"details_item0_label","component":"Text","content":"耳机盒","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/earphone/batteryLevel} + '% ' + ${/data/earphone/chargingStatusDesc} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item0","component":"Row","children":["details_item0_label","details_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row0","component":"Row","children":["details_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"details_item1_label","component":"Text","content":"左耳","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/earphone/leftBatteryLevel} + '% ' + ${/data/earphone/leftChargingStatusDesc} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item1","component":"Row","children":["details_item1_label","details_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row1","component":"Row","children":["details_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"details_item2_label","component":"Text","content":"右耳","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/earphone/rightBatteryLevel} + '% ' + ${/data/earphone/rightChargingStatusDesc} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"details_item2","component":"Row","children":["details_item2_label","details_item2_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"details_row2","component":"Row","children":["details_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"earphone":{"isConnected":true,"earphoneName":"示例耳机","batteryLevel":80,"chargingStatusDesc":"未充电","leftBatteryLevel":76,"leftChargingStatusDesc":"未充电","rightBatteryLevel":78,"rightChargingStatusDesc":"未充电"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建耳机卡片，展示耳机连接状态、设备名称、耳机盒电量、左右耳机电量及充电状态",
  "size": "2x2",
  "appVersion": "11.7.8.303",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "earphone": {
        "isConnected": {
          "type": "boolean",
          "description": "当前是否有蓝牙耳机处于连接活跃状态。",
          "sampleValue": true
        },
        "earphoneName": {
          "type": "string",
          "description": "耳机的设备广播名称，如果未连接则返回'未连接耳机'。如: 'FreeBuds Pro 3'。",
          "sampleValue": "示例耳机"
        },
        "batteryLevel": {
          "type": "integer",
          "description": "耳机盒（或整体）当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 80
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "耳机盒（或整体）当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "leftBatteryLevel": {
          "type": "integer",
          "description": "左耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 76
        },
        "leftChargingStatusDesc": {
          "type": "string",
          "description": "左耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "rightBatteryLevel": {
          "type": "integer",
          "description": "右耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 78
        },
        "rightChargingStatusDesc": {
          "type": "string",
          "description": "右耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_bluetooth_earbuds_black",
      "src": "resources/base/media/emoji_bluetooth_earbuds_black.png",
      "description": "样式：深灰到黑色渐变的一对分体式入耳蓝牙耳机，带立体高光与透明背景，原始尺寸为 64×64，PNG 位图需保留原色；适用：蓝牙耳机连接状态、名称或左右耳电量卡片，可结合 GetEarphoneInfo 的 isConnected、earphoneName、leftBatteryLevel 和 rightBatteryLevel 展示，也可作为 event.open.settings.bluetooth 的蓝牙设置入口。图标不表示耳机当前已连接、正在充电或具有特定电量。"
    },
    {
      "id": "asset.emoji_earbud_case_black",
      "src": "resources/base/media/emoji_earbud_case_black.png",
      "description": "样式：深灰到黑色渐变的封闭式蓝牙耳机充电盒，盒体呈圆润横向椭圆并带高光，透明背景，原始尺寸为 64×64，PNG 位图需保留原色；适用：蓝牙耳机盒或整体电量与充电状态卡片，可结合 GetEarphoneInfo 的 batteryLevel 和 chargingStatusDesc 展示，也可作为 event.open.settings.bluetooth 的蓝牙设置入口。图标不表示耳机盒当前正在充电、已经打开或具有特定电量。"
    },
    {
      "id": "asset.ic_Bluetooth",
      "src": "resources/base/media/ic_Bluetooth.svg",
      "description": "样式：默认黑色的单色蓝牙标志图标，原始尺寸为 24×24；适用：蓝牙设备连接卡片中配合 GetEarphoneInfo 展示蓝牙耳机连接状态，也可作为 event.open.settings.bluetooth 或 event.setBluetoothMode 的蓝牙设置与开关入口。图标本身不表示当前已连接、已开启或已关闭状态。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetEarphoneInfo"
  ],
  "event": [],
  "asset": [
    "asset.emoji_bluetooth_earbuds_black",
    "asset.emoji_earbud_case_black",
    "asset.ic_Bluetooth"
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
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/isConnected",
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.emoji_bluetooth_earbuds_black",
    "asset.emoji_earbud_case_black",
    "asset.ic_Bluetooth"
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
  "artifactId": "68ba51f3-36bd-418c-a1ff-74270a3815c3",
  "createdAt": 1793952204080
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","status","details"]]
["title","SingleLineTitle",{"title":{"path":"/data/earphone/earphoneName"},"icon":"resources/base/media/emoji_bluetooth_earbuds_black.png","fontSize":12}]
["status","EmphasisText",{"mainText":"{{ ${/data/earphone/isConnected} ? '已连接' : '未连接' }}","fontSize":18}]
["details","SecondaryBody",{"columns":1,"items":[{"label":"耳机盒","value":"{{ ${/data/earphone/batteryLevel} + '% ' + ${/data/earphone/chargingStatusDesc} }}"},{"label":"左耳","value":"{{ ${/data/earphone/leftBatteryLevel} + '% ' + ${/data/earphone/leftChargingStatusDesc} }}"},{"label":"右耳","value":"{{ ${/data/earphone/rightBatteryLevel} + '% ' + ${/data/earphone/rightChargingStatusDesc} }}"}],"fontSize":12}]
["/data/earphone/isConnected",true]
["/data/earphone/earphoneName","示例耳机"]
["/data/earphone/batteryLevel",80]
["/data/earphone/chargingStatusDesc","未充电"]
["/data/earphone/leftBatteryLevel",76]
["/data/earphone/leftChargingStatusDesc","未充电"]
["/data/earphone/rightBatteryLevel",78]
["/data/earphone/rightChargingStatusDesc","未充电"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "HOP-AL10 7.0.0.109",
    "candidateAssetIds": [
      "asset.emoji_bluetooth_earbuds_black",
      "asset.emoji_earbud_case_black",
      "asset.ic_Bluetooth"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "连接与电量速览",
    "userQuery": "创建耳机卡片，展示耳机连接状态、设备名称、耳机盒电量、左右耳机电量及充电状态",
    "title": "耳机状态",
    "candidateDataBindings": [
      {
        "capabilityId": "GetEarphoneInfo",
        "arguments": {},
        "writeResultTo": "/data/earphone",
        "candidateOutputFields": [
          "/isConnected",
          "/earphoneName",
          "/batteryLevel",
          "/chargingStatusDesc",
          "/leftBatteryLevel",
          "/leftChargingStatusDesc",
          "/rightBatteryLevel",
          "/rightChargingStatusDesc"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "ohos",
    "prdVer": "11.7.8.303",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261104090602633"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q456-000",
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
  "romVersion": "HOP-AL10 7.0.0.109",
  "candidateAssetIds": [
    "asset.emoji_bluetooth_earbuds_black",
    "asset.emoji_earbud_case_black",
    "asset.ic_Bluetooth"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "连接与电量速览",
  "userQuery": "创建耳机卡片，展示耳机连接状态、设备名称、耳机盒电量、左右耳机电量及充电状态",
  "title": "耳机状态",
  "candidateDataBindings": [
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/isConnected",
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc"
      ]
    }
  ]
}
```
