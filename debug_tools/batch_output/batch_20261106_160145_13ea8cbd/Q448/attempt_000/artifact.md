```cardspec
{
  "title": "家人纪念日",
  "description": "家人重要日子提醒",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-10-15"
      },
      "writeResultTo": "/data/countdown0"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-07-04"
      },
      "writeResultTo": "/data/countdown1"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-29"
      },
      "writeResultTo": "/data/countdown2"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-22"
      },
      "writeResultTo": "/data/countdown3"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-11-08"
      },
      "writeResultTo": "/data/countdown4"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-01-23"
      },
      "writeResultTo": "/data/countdown5"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"primary_title","component":"Text","content":"家人重要日子","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#998C4B1C"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Column","children":["details_item0","details_item1","details_item2"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":102}}},{"id":"details_item0","component":"Row","children":["details_item0_text"],"styles":{"width":"matchParent","height":28,"padding":{"left":12,"right":12},"borderRadius":8,"backgroundColor":"#99FFFFFF","alignItems":"center","flexShrink":0},"itemMargin":0},{"id":"details_item0_text","component":"Text","content":"{{ '奶奶生日 10月15日 · ' + ${/data/countdown0/countdownDays} + '天' }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":400,"maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}},{"id":"details_item1","component":"Row","children":["details_item1_text"],"styles":{"width":"matchParent","height":28,"padding":{"left":12,"right":12},"borderRadius":8,"backgroundColor":"#99FFFFFF","alignItems":"center","flexShrink":0},"itemMargin":0},{"id":"details_item1_text","component":"Text","content":"{{ '爷爷生日 7月4日 · ' + ${/data/countdown1/countdownDays} + '天' }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":400,"maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}},{"id":"details_item2","component":"Row","children":["details_item2_text"],"styles":{"width":"matchParent","height":28,"padding":{"left":12,"right":12},"borderRadius":8,"backgroundColor":"#99FFFFFF","alignItems":"center","flexShrink":0},"itemMargin":0},{"id":"details_item2_text","component":"Text","content":"{{ '爸爸生日 4月29日 · ' + ${/data/countdown2/countdownDays} + '天' }}","styles":{"width":"matchParent","fontSize":12,"fontWeight":400,"maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"countdown0":{"countdownDays":30},"countdown1":{"countdownDays":30},"countdown2":{"countdownDays":30},"countdown3":{"countdownDays":30},"countdown4":{"countdownDays":30},"countdown5":{"countdownDays":30}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "制作一张家人重要日子倒计时卡片，标注每位家人的名字和对应的公历日期。奶奶生日：2026年10月15日（农历九月初六）；爷爷生日：2026年7月4日（农历五月二十）；爸爸生日：2026年4月29日（农历三月十三）；妈妈生日：2026年4月22日（农历三月初六）；崔景会生日：2026年11月8日（农历九月三十）；父母结婚纪念日：2027年1月23日（农历腊月十六）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶生日10月15日、爷爷生日7月4日、爸爸生日4月29日、妈妈生日4月22日、崔景会生日11月8日、父母结婚纪念日1月23日",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "countdown0": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      },
      "countdown1": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      },
      "countdown2": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      },
      "countdown3": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      },
      "countdown4": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
        }
      },
      "countdown5": {
        "countdownDays": {
          "type": "integer",
          "description": "距离目标日期的自然日天数纯整数，返回值不包含“天”。正数表示未来，0 表示今天，负数表示已经过去；若直接用于文本展示，必须在数值后追加“天”。",
          "sampleValue": 30
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
    "GetCountdownDays",
    "GetCountdownDays",
    "GetCountdownDays",
    "GetCountdownDays",
    "GetCountdownDays",
    "GetCountdownDays"
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
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-10-15"
      },
      "writeResultTo": "/data/countdown0",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-07-04"
      },
      "writeResultTo": "/data/countdown1",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-29"
      },
      "writeResultTo": "/data/countdown2",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-22"
      },
      "writeResultTo": "/data/countdown3",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-11-08"
      },
      "writeResultTo": "/data/countdown4",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-01-23"
      },
      "writeResultTo": "/data/countdown5",
      "candidateOutputFields": [
        "/countdownDays"
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
  "artifactId": "36229a17-1e3e-415e-851f-011aa4a106ed",
  "createdAt": 1793952187529
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["primary","details"]]
["primary","SingleLineTitle",{"title":"家人重要日子","fontSize":12}]
["details","SummaryList",{"items":["{{ '奶奶生日 10月15日 · ' + ${/data/countdown0/countdownDays} + '天' }}","{{ '爷爷生日 7月4日 · ' + ${/data/countdown1/countdownDays} + '天' }}","{{ '爸爸生日 4月29日 · ' + ${/data/countdown2/countdownDays} + '天' }}"]}]
["/data/countdown0/countdownDays",30]
["/data/countdown1/countdownDays",30]
["/data/countdown2/countdownDays",30]
["/data/countdown3/countdownDays",30]
["/data/countdown4/countdownDays",30]
["/data/countdown5/countdownDays",30]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "家人重要日子提醒",
    "userQuery": "制作一张家人重要日子倒计时卡片，标注每位家人的名字和对应的公历日期。奶奶生日：2026年10月15日（农历九月初六）；爷爷生日：2026年7月4日（农历五月二十）；爸爸生日：2026年4月29日（农历三月十三）；妈妈生日：2026年4月22日（农历三月初六）；崔景会生日：2026年11月8日（农历九月三十）；父母结婚纪念日：2027年1月23日（农历腊月十六）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶生日10月15日、爷爷生日7月4日、爸爸生日4月29日、妈妈生日4月22日、崔景会生日11月8日、父母结婚纪念日1月23日",
    "title": "家人纪念日",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2026-10-15"
        },
        "writeResultTo": "/data/countdown0",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2026-07-04"
        },
        "writeResultTo": "/data/countdown1",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2026-04-29"
        },
        "writeResultTo": "/data/countdown2",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2026-04-22"
        },
        "writeResultTo": "/data/countdown3",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2026-11-08"
        },
        "writeResultTo": "/data/countdown4",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-01-23"
        },
        "writeResultTo": "/data/countdown5",
        "candidateOutputFields": [
          "/countdownDays"
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
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261103015222076"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q448-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "家人重要日子提醒",
  "userQuery": "制作一张家人重要日子倒计时卡片，标注每位家人的名字和对应的公历日期。奶奶生日：2026年10月15日（农历九月初六）；爷爷生日：2026年7月4日（农历五月二十）；爸爸生日：2026年4月29日（农历三月十三）；妈妈生日：2026年4月22日（农历三月初六）；崔景会生日：2026年11月8日（农历九月三十）；父母结婚纪念日：2027年1月23日（农历腊月十六）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶生日10月15日、爷爷生日7月4日、爸爸生日4月29日、妈妈生日4月22日、崔景会生日11月8日、父母结婚纪念日1月23日",
  "title": "家人纪念日",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-10-15"
      },
      "writeResultTo": "/data/countdown0",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-07-04"
      },
      "writeResultTo": "/data/countdown1",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-29"
      },
      "writeResultTo": "/data/countdown2",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-04-22"
      },
      "writeResultTo": "/data/countdown3",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2026-11-08"
      },
      "writeResultTo": "/data/countdown4",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-01-23"
      },
      "writeResultTo": "/data/countdown5",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"primary\",\"details\"]]\n[\"primary\",\"SingleLineTitle\",{\"title\":\"家人重要日子\",\"fontSize\":12}]\n[\"details\",\"SummaryList\",{\"items\":[\"{{ '奶奶生日 10月15日 · ' + ${/data/countdown0/countdownDays} + '天' }}\",\"{{ '爷爷生日 7月4日 · ' + ${/data/countdown1/countdownDays} + '天' }}\",\"{{ '爸爸生日 4月29日 · ' + ${/data/countdown2/countdownDays} + '天' }}\"]}]\n[\"/data/countdown0/countdownDays\",30]\n[\"/data/countdown1/countdownDays\",30]\n[\"/data/countdown2/countdownDays\",30]\n[\"/data/countdown3/countdownDays\",30]\n[\"/data/countdown4/countdownDays\",30]\n[\"/data/countdown5/countdownDays\",30]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Row\",\"children\":[\"primary_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"primary_title\",\"component\":\"Text\",\"content\":\"家人重要日子\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Column\",\"children\":[\"details_item0\",\"details_item1\",\"details_item2\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"end\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":102}}},{\"id\":\"details_item0\",\"component\":\"Row\",\"children\":[\"details_item0_text\"],\"styles\":{\"width\":\"matchParent\",\"height\":28,\"padding\":{\"left\":12,\"right\":12},\"borderRadius\":8,\"backgroundColor\":\"@theme:panel/1\",\"alignItems\":\"center\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_text\",\"component\":\"Text\",\"content\":\"{{ '奶奶生日 10月15日 · ' + ${/data/countdown0/countdownDays} + '天' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Row\",\"children\":[\"details_item1_text\"],\"styles\":{\"width\":\"matchParent\",\"height\":28,\"padding\":{\"left\":12,\"right\":12},\"borderRadius\":8,\"backgroundColor\":\"@theme:panel/1\",\"alignItems\":\"center\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_text\",\"component\":\"Text\",\"content\":\"{{ '爷爷生日 7月4日 · ' + ${/data/countdown1/countdownDays} + '天' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item2\",\"component\":\"Row\",\"children\":[\"details_item2_text\"],\"styles\":{\"width\":\"matchParent\",\"height\":28,\"padding\":{\"left\":12,\"right\":12},\"borderRadius\":8,\"backgroundColor\":\"@theme:panel/1\",\"alignItems\":\"center\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_text\",\"component\":\"Text\",\"content\":\"{{ '爸爸生日 4月29日 · ' + ${/data/countdown2/countdownDays} + '天' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"countdown0\":{\"countdownDays\":30},\"countdown1\":{\"countdownDays\":30},\"countdown2\":{\"countdownDays\":30},\"countdown3\":{\"countdownDays\":30},\"countdown4\":{\"countdownDays\":30},\"countdown5\":{\"countdownDays\":30}}}}}",
  "validationErrors": []
}
```
