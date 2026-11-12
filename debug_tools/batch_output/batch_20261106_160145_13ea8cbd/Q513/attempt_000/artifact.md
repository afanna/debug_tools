```cardspec
{
  "title": "家人纪念日",
  "description": "家人重要日子倒计时",
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
        "targetDate": "2027-10-05"
      },
      "writeResultTo": "/data/countdown0"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-06-24"
      },
      "writeResultTo": "/data/countdown1"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-19"
      },
      "writeResultTo": "/data/countdown2"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-12"
      },
      "writeResultTo": "/data/countdown3"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2028-01-12"
      },
      "writeResultTo": "/data/countdown4"
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-10-28"
      },
      "writeResultTo": "/data/countdown5"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFFFE0CC",0],["#FFFFF7F2",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"家人重要日子倒计时","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#998C4B1C"}},{"id":"title_icon","component":"Image","src":"resources/base/media/cake_fill.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF8C4B1C"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_row0","primary_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"primary_item0_label","component":"Text","content":"奶奶/爷爷","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#998C4B1C","textOverflow":"clip"}},{"id":"primary_item0_value","component":"Text","content":"{{ ${/data/countdown0/countdownDays} + '天 · 10月5日' }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF8C4B1C","layoutWeight":1,"textOverflow":"clip"}},{"id":"primary_item0","component":"Row","children":["primary_item0_label","primary_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"primary_row0","component":"Row","children":["primary_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"primary_item1_label","component":"Text","content":"爸爸","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#998C4B1C","textOverflow":"clip"}},{"id":"primary_item1_value","component":"Text","content":"{{ ${/data/countdown1/countdownDays} + '天 · 6月24日' }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF8C4B1C","layoutWeight":1,"textOverflow":"clip"}},{"id":"primary_item1","component":"Row","children":["primary_item1_label","primary_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"primary_row1","component":"Row","children":["primary_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1","details_item2","details_item3"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"妈妈","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#998C4B1C"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/countdown2/countdownDays} + '天 · 4月19日' }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"崔景会","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#998C4B1C"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/countdown3/countdownDays} + '天 · 4月12日' }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}},{"id":"details_item2","component":"Column","children":["details_item2_label_slot","details_item2_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item2_label_slot","component":"Row","children":["details_item2_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_label","component":"Text","content":"爸妈结婚纪念日","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#998C4B1C"}},{"id":"details_item2_value_slot","component":"Row","children":["details_item2_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/countdown4/countdownDays} + '天 · 1月12日' }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}},{"id":"details_item3","component":"Column","children":["details_item3_label_slot","details_item3_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item3_label_slot","component":"Row","children":["details_item3_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item3_label","component":"Text","content":"我的生日","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#998C4B1C"}},{"id":"details_item3_value_slot","component":"Row","children":["details_item3_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item3_value","component":"Text","content":"{{ ${/data/countdown5/countdownDays} + '天 · 10月28日' }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF8C4B1C"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"countdown0":{"countdownDays":30},"countdown1":{"countdownDays":30},"countdown2":{"countdownDays":30},"countdown3":{"countdownDays":30},"countdown4":{"countdownDays":30},"countdown5":{"countdownDays":30}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张家人重要日子倒计时卡片，每天自动更新倒计时天数，标注每位家人的名字和对应的公历日期。奶奶/爷爷生日：2027年10月5日（农历九月初六）；爸爸生日：2027年6月24日（农历五月二十）；妈妈生日：2027年4月19日（农历三月十三）；崔景会生日：2027年4月12日（农历三月初六）；爸妈结婚纪念日：2028年1月12日（农历腊月十六）；我的生日：2027年10月28日（农历九月廿九，2027年农历九月无三十）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶/爷爷生日10月5日、爸爸生日6月24日、妈妈生日4月19日、崔景会生日4月12日、爸妈结婚纪念日1月12日、我的生日10月28日",
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
  "assetCandidates": [
    {
      "id": "asset.cake_fill",
      "src": "resources/base/media/cake_fill.svg",
      "description": "样式：默认黑色的单色实心生日蛋糕图标，顶部带蜡烛，原始尺寸为 24×24；适用：生日、纪念日、节日、庆祝事件与运动目标达成。"
    }
  ]
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
  "asset": [
    "asset.cake_fill"
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
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-10-05"
      },
      "writeResultTo": "/data/countdown0",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-06-24"
      },
      "writeResultTo": "/data/countdown1",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-19"
      },
      "writeResultTo": "/data/countdown2",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-12"
      },
      "writeResultTo": "/data/countdown3",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2028-01-12"
      },
      "writeResultTo": "/data/countdown4",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-10-28"
      },
      "writeResultTo": "/data/countdown5",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.cake_fill"
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
  "artifactId": "a69dc10f-e1fb-464e-93ab-2ebec5ba2b80",
  "createdAt": 1793952366721
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"家人重要日子倒计时","icon":"resources/base/media/cake_fill.svg","fontSize":12}]
["primary","SecondaryBody",{"columns":2,"items":[{"label":"奶奶/爷爷 ","value":"{{ ${/data/countdown0/countdownDays} + '天 · 10月5日' }}"},{"label":"爸爸 ","value":"{{ ${/data/countdown1/countdownDays} + '天 · 6月24日' }}"}],"fontSize":14}]
["details","TextBlock",{"items":[{"label":"妈妈","value":"{{ ${/data/countdown2/countdownDays} + '天 · 4月19日' }}"},{"label":"崔景会","value":"{{ ${/data/countdown3/countdownDays} + '天 · 4月12日' }}"},{"label":"爸妈结婚纪念日","value":"{{ ${/data/countdown4/countdownDays} + '天 · 1月12日' }}"},{"label":"我的生日","value":"{{ ${/data/countdown5/countdownDays} + '天 · 10月28日' }}"}]}]
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
    "candidateAssetIds": [
      "asset.cake_fill"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "家人重要日子倒计时",
    "userQuery": "创建一张家人重要日子倒计时卡片，每天自动更新倒计时天数，标注每位家人的名字和对应的公历日期。奶奶/爷爷生日：2027年10月5日（农历九月初六）；爸爸生日：2027年6月24日（农历五月二十）；妈妈生日：2027年4月19日（农历三月十三）；崔景会生日：2027年4月12日（农历三月初六）；爸妈结婚纪念日：2028年1月12日（农历腊月十六）；我的生日：2027年10月28日（农历九月廿九，2027年农历九月无三十）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶/爷爷生日10月5日、爸爸生日6月24日、妈妈生日4月19日、崔景会生日4月12日、爸妈结婚纪念日1月12日、我的生日10月28日",
    "title": "家人纪念日",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-10-05"
        },
        "writeResultTo": "/data/countdown0",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-06-24"
        },
        "writeResultTo": "/data/countdown1",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-04-19"
        },
        "writeResultTo": "/data/countdown2",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-04-12"
        },
        "writeResultTo": "/data/countdown3",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2028-01-12"
        },
        "writeResultTo": "/data/countdown4",
        "candidateOutputFields": [
          "/countdownDays"
        ]
      },
      {
        "capabilityId": "GetCountdownDays",
        "arguments": {
          "targetDate": "2027-10-28"
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
    "time": "20261103015744026"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q513-000",
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
  "candidateAssetIds": [
    "asset.cake_fill"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "家人重要日子倒计时",
  "userQuery": "创建一张家人重要日子倒计时卡片，每天自动更新倒计时天数，标注每位家人的名字和对应的公历日期。奶奶/爷爷生日：2027年10月5日（农历九月初六）；爸爸生日：2027年6月24日（农历五月二十）；妈妈生日：2027年4月19日（农历三月十三）；崔景会生日：2027年4月12日（农历三月初六）；爸妈结婚纪念日：2028年1月12日（农历腊月十六）；我的生日：2027年10月28日（农历九月廿九，2027年农历九月无三十）。\n本轮卡片静态内容（用作展示的外部事实）：奶奶/爷爷生日10月5日、爸爸生日6月24日、妈妈生日4月19日、崔景会生日4月12日、爸妈结婚纪念日1月12日、我的生日10月28日",
  "title": "家人纪念日",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-10-05"
      },
      "writeResultTo": "/data/countdown0",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-06-24"
      },
      "writeResultTo": "/data/countdown1",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-19"
      },
      "writeResultTo": "/data/countdown2",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-04-12"
      },
      "writeResultTo": "/data/countdown3",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2028-01-12"
      },
      "writeResultTo": "/data/countdown4",
      "candidateOutputFields": [
        "/countdownDays"
      ]
    },
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-10-28"
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
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"家人重要日子倒计时\",\"icon\":\"resources/base/media/cake_fill.svg\",\"fontSize\":12}]\n[\"primary\",\"SecondaryBody\",{\"columns\":2,\"items\":[{\"label\":\"奶奶/爷爷 \",\"value\":\"{{ ${/data/countdown0/countdownDays} + '天 · 10月5日' }}\"},{\"label\":\"爸爸 \",\"value\":\"{{ ${/data/countdown1/countdownDays} + '天 · 6月24日' }}\"}],\"fontSize\":14}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"妈妈\",\"value\":\"{{ ${/data/countdown2/countdownDays} + '天 · 4月19日' }}\"},{\"label\":\"崔景会\",\"value\":\"{{ ${/data/countdown3/countdownDays} + '天 · 4月12日' }}\"},{\"label\":\"爸妈结婚纪念日\",\"value\":\"{{ ${/data/countdown4/countdownDays} + '天 · 1月12日' }}\"},{\"label\":\"我的生日\",\"value\":\"{{ ${/data/countdown5/countdownDays} + '天 · 10月28日' }}\"}]}]\n[\"/data/countdown0/countdownDays\",30]\n[\"/data/countdown1/countdownDays\",30]\n[\"/data/countdown2/countdownDays\",30]\n[\"/data/countdown3/countdownDays\",30]\n[\"/data/countdown4/countdownDays\",30]\n[\"/data/countdown5/countdownDays\",30]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\",\"title_icon\"],\"styles\":{\"width\":\"matchParent\",\"height\":20,\"flexShrink\":0,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"家人重要日子倒计时\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":1,\"width\":\"wrapContent\",\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"title_icon\",\"component\":\"Image\",\"src\":\"resources/base/media/cake_fill.svg\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"flexShrink\":0,\"fillColor\":\"@theme:graphicPrimary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_row0\",\"primary_row1\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"primary_item0_label\",\"component\":\"Text\",\"content\":\"奶奶/爷爷\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown0/countdownDays} + '天 · 10月5日' }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"primary_item0\",\"component\":\"Row\",\"children\":[\"primary_item0_label\",\"primary_item0_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"primary_row0\",\"component\":\"Row\",\"children\":[\"primary_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"primary_item1_label\",\"component\":\"Text\",\"content\":\"爸爸\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown1/countdownDays} + '天 · 6月24日' }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"primary_item1\",\"component\":\"Row\",\"children\":[\"primary_item1_label\",\"primary_item1_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"primary_row1\",\"component\":\"Row\",\"children\":[\"primary_item1\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_item0\",\"details_item1\",\"details_item2\",\"details_item3\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"top\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":48}}},{\"id\":\"details_item0\",\"component\":\"Column\",\"children\":[\"details_item0_label_slot\",\"details_item0_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item0_label_slot\",\"component\":\"Row\",\"children\":[\"details_item0_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_label\",\"component\":\"Text\",\"content\":\"妈妈\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item0_value_slot\",\"component\":\"Row\",\"children\":[\"details_item0_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown2/countdownDays} + '天 · 4月19日' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Column\",\"children\":[\"details_item1_label_slot\",\"details_item1_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item1_label_slot\",\"component\":\"Row\",\"children\":[\"details_item1_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_label\",\"component\":\"Text\",\"content\":\"崔景会\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item1_value_slot\",\"component\":\"Row\",\"children\":[\"details_item1_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown3/countdownDays} + '天 · 4月12日' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item2\",\"component\":\"Column\",\"children\":[\"details_item2_label_slot\",\"details_item2_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item2_label_slot\",\"component\":\"Row\",\"children\":[\"details_item2_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_label\",\"component\":\"Text\",\"content\":\"爸妈结婚纪念日\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item2_value_slot\",\"component\":\"Row\",\"children\":[\"details_item2_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown4/countdownDays} + '天 · 1月12日' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item3\",\"component\":\"Column\",\"children\":[\"details_item3_label_slot\",\"details_item3_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item3_label_slot\",\"component\":\"Row\",\"children\":[\"details_item3_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item3_label\",\"component\":\"Text\",\"content\":\"我的生日\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item3_value_slot\",\"component\":\"Row\",\"children\":[\"details_item3_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item3_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/countdown5/countdownDays} + '天 · 10月28日' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"countdown0\":{\"countdownDays\":30},\"countdown1\":{\"countdownDays\":30},\"countdown2\":{\"countdownDays\":30},\"countdown3\":{\"countdownDays\":30},\"countdown4\":{\"countdownDays\":30},\"countdown5\":{\"countdownDays\":30}}}}}",
  "validationErrors": []
}
```
