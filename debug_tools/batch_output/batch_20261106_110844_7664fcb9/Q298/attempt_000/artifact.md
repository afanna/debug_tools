```cardspec
{
  "title": "血氧监测",
  "description": "实时血氧数据",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/health"
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery"
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    },
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["fusionBallBackground","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#00000000"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F1F99","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF2B65D9","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF57AED9","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/time/currentDate} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#CCFFFFFF"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main","primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/health/sleepScore} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"primary_secondary","component":"Text","content":"{{ '心率 ' + ${/data/health/exerciseHeartRateAvg} + '次/分钟' }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0","support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"星期","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/time/dayOfWeek} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FFFFFFFF","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item1_label","component":"Text","content":"电量","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"support_item1_value","component":"Text","content":"{{ ${/data/battery/batterySOCText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FFFFFFFF","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item1","component":"Row","children":["support_item1_label","support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row1","component":"Row","children":["support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例"},"health":{"sleepScore":82,"exerciseHeartRateAvg":135},"battery":{"batterySOCText":"68%"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "按照用户提供的图片风格设计一个血氧显示页面卡片，显示血氧数据。图片风格为：蓝色星空背景，显示日期、时间、心率、血氧、电量信息。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "health": {
        "targetDateText": {
          "type": "string",
          "description": "该组健康与运动数据所归属的确切日期文本，格式为 YYYY-MM-DD，例如 '2026-07-06'。用于明确展示当前查阅的是哪一天的数据。",
          "sampleValue": "2026-08-06"
        },
        "sleepScore": {
          "type": "integer",
          "description": "睡眠综合得分，取值范围 0-100。",
          "sampleValue": 82
        },
        "sleepStatus": {
          "type": "string",
          "description": "基于得分智能生成的睡眠状态语义判定，包括：'优秀'、'良好'、'一般'、'较差'。",
          "sampleValue": "良好"
        },
        "sleepTypeDesc": {
          "type": "string",
          "description": "睡眠记录方式或类型的描述，例如“科学睡眠”、“普通睡眠”、“手动输入睡眠”、“手机记录睡眠”。",
          "sampleValue": "科学睡眠"
        },
        "nightSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“7小时1分”。",
          "sampleValue": "7小时1分"
        },
        "deepSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠深睡总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“2小时15分”。",
          "sampleValue": "2小时15分"
        },
        "totalNapDurationText": {
          "type": "string",
          "description": "可直接显示的白天零星小睡累计总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“45分”或“0分”。",
          "sampleValue": "0分"
        },
        "fallAsleepTimeText": {
          "type": "string",
          "description": "格式化后的确切入睡时刻短文本（HH:mm），例如“23:15”。",
          "sampleValue": "23:15"
        },
        "wakeupTimeText": {
          "type": "string",
          "description": "格式化后的确切醒来时刻短文本（HH:mm），例如“07:30”。",
          "sampleValue": "07:30"
        },
        "dailySteps": {
          "type": "integer",
          "description": "与最新睡眠同属一天的日常全天累计活动总步数纯整数，返回值不包含“步”。若直接用于文本展示，必须在数值后追加“步”。",
          "sampleValue": 6200
        },
        "dailyTotalCaloriesText": {
          "type": "string",
          "description": "可直接显示的日常活动总消耗热量文本，已完成千分位归一化并包含“千卡”单位；展示时不得再次追加热量单位。例如“998 千卡”。",
          "sampleValue": "420 千卡"
        },
        "dailyDistanceText": {
          "type": "string",
          "description": "可直接显示的日常活动总距离文本，端侧已根据数值大小换算并包含“米”或“公里”单位；展示时不得再次追加距离单位。例如“5.42 公里”或“755 米”。",
          "sampleValue": "4.60 公里"
        },
        "exerciseTypeName": {
          "type": "string",
          "description": "最近一次发生的单次专业运动训练类型的中文映射名称，如“羽毛球”、“自由训练”、“户外跑步”。若无记录则返回“暂无运动”。",
          "sampleValue": "户外跑步"
        },
        "exerciseStartTimeText": {
          "type": "string",
          "description": "专业运动开始的确切时刻文本（HH:mm），例如“18:30”。",
          "sampleValue": "18:30"
        },
        "exerciseEndTimeText": {
          "type": "string",
          "description": "专业运动结束的确切时刻文本（HH:mm），例如“19:50”。",
          "sampleValue": "19:10"
        },
        "exerciseDurationText": {
          "type": "string",
          "description": "可直接显示的单次专业运动实际持续时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“1小时40分”。",
          "sampleValue": "40分"
        },
        "exerciseCalorieText": {
          "type": "string",
          "description": "可直接显示的单次专业运动净热量消耗文本，已换算并包含“千卡”单位；展示时不得再次追加热量单位。例如“98 千卡”。",
          "sampleValue": "260 千卡"
        },
        "exerciseHeartRateAvg": {
          "type": "integer",
          "description": "专业运动期间平均心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 135
        },
        "exerciseHeartRateMax": {
          "type": "integer",
          "description": "专业运动期间最大心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 168
        },
        "exerciseHeartRateMin": {
          "type": "integer",
          "description": "专业运动期间最低心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 96
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成多实体规整转换的系统格式化时间戳字符串，如 '2026-07-03 14:57'。",
          "sampleValue": "2026-08-06 09:00"
        }
      },
      "battery": {
        "batterySOCText": {
          "type": "string",
          "description": "可直接显示的当前手机设备剩余电量文本，已包含“%”单位；展示时不得再次追加“%”。",
          "sampleValue": "68%",
          "numericSource": "/data/battery/batterySOC"
        },
        "batterySOC": {
          "type": "integer",
          "description": "当前手机设备剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”；优先使用 batterySOCText。",
          "sampleValue": 68
        }
      },
      "time": {
        "currentDate": {
          "type": "string",
          "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
          "sampleValue": "示例"
        },
        "dayOfWeek": {
          "type": "string",
          "description": "中文的星期描述，例如 '星期四'。",
          "sampleValue": "示例"
        }
      },
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
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成多源数据感知和融合的时间戳字符串。如：2026-07-02 20:15",
          "sampleValue": "2026-08-06 09:00"
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
    "GetHealthAndSportSummary",
    "GetPhoneBatteryInfo",
    "GetCurrentTime",
    "GetEarphoneInfo"
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
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/health",
      "candidateOutputFields": []
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/batterySOC"
      ]
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek"
      ]
    },
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": []
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
  "artifactId": "20f5e0ce-c78c-4265-96c7-6e73325dc7f8",
  "createdAt": 1793934541577
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":{"path":"/data/time/currentDate"},"fontSize":12}]
["primary","EmphasisText",{"mainText":{"path":"/data/health/sleepScore"},"secondaryText":"{{ '心率 ' + ${/data/health/exerciseHeartRateAvg} + '次/分钟' }}","fontSize":18}]
["support","SecondaryBody",{"items":[{"label":"星期 ","value":{"path":"/data/time/dayOfWeek"}},{"label":"电量 ","value":{"path":"/data/battery/batterySOCText"}}],"columns":1,"fontSize":12}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/health/sleepScore",82]
["/data/health/exerciseHeartRateAvg",135]
["/data/battery/batterySOCText","68%"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "按照用户提供的图片风格设计一个血氧显示页面卡片，显示血氧数据。图片风格为：蓝色星空背景，显示日期、时间、心率、血氧、电量信息。",
    "candidateDataBindings": [
      {
        "capabilityId": "GetHealthAndSportSummary",
        "arguments": {},
        "writeResultTo": "/data/health"
      },
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/battery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/batterySOC"
        ]
      },
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek"
        ]
      },
      {
        "capabilityId": "GetEarphoneInfo",
        "arguments": {},
        "writeResultTo": "/data/earphone"
      }
    ],
    "title": "血氧监测",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "实时血氧数据",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261029025410294"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q298-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "按照用户提供的图片风格设计一个血氧显示页面卡片，显示血氧数据。图片风格为：蓝色星空背景，显示日期、时间、心率、血氧、电量信息。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "按照用户提供的图片风格设计一个血氧显示页面卡片，显示血氧数据。图片风格为：蓝色星空背景，显示日期、时间、心率、血氧、电量信息。",
  "candidateDataBindings": [
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/health"
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/battery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/batterySOC"
      ]
    },
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek"
      ]
    },
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone"
    }
  ],
  "title": "血氧监测",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "实时血氧数据",
  "candidateAssetIds": []
}
```
