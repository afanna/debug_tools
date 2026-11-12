```cardspec
{
  "title": "春节倒计时",
  "description": "距离春节还有多少天",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCountdownDays",
      "arguments": {
        "targetDate": "2027-02-06"
      },
      "writeResultTo": "/data/countdown"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["__post_theme_background","template_root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"borderRadius":18,"clip":true,"alignContent":"topStart","backgroundColor":"#00000000"}},{"id":"__post_theme_background","component":"Stack","children":["__post_theme_base"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"__post_theme_base","component":"Image","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/833c5de3326049de993cc193a526df84/cbfe92acc718409aae519be674465497.jpg","styles":{"width":"matchParent","height":"matchParent","objectFit":"fill"}},{"id":"template_root","component":"Stack","children":["__genui_render_component__template_root"],"styles":{"width":"matchParent","height":"matchParent","padding":12}},{"id":"__genui_render_component__template_root","component":"Stack","children":["root_1"],"styles":{"width":"matchParent","height":"matchParent"}},{"id":"root_1","component":"Stack","children":["root_1_0"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"root_1_0","component":"Column","children":["root_1_0_0","root_1_0_1"],"styles":{"width":"matchParent","height":"matchParent","justifyContent":"spaceBetween","alignItems":"center","constraintSize":{"minWidth":0,"minHeight":0}},"itemMargin":0},{"id":"root_1_0_0","component":"Column","children":["root_1_0_0_0","root_1_0_0_1"],"styles":{"width":"matchParent","justifyContent":"start","alignItems":"center","constraintSize":{"minWidth":0,"minHeight":0}},"itemMargin":0},{"id":"root_1_0_0_0","component":"Text","content":"春节还剩","styles":{"width":"matchParent","height":24,"margin":{"top":4},"fontSize":12,"minFontSize":12,"fontWeight":500,"fontColor":"#CCFFFFFF","maxLines":1,"textAlign":"center","textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"root_1_0_0_1","component":"Text","content":"{{ ${/data/countdown/countdownDays} }}","styles":{"height":58,"margin":{"top":8},"fontSize":48,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"root_1_0_1","component":"Text","content":"天","styles":{"height":16,"fontSize":12,"fontWeight":500,"fontColor":"#CCFFFFFF","maxLines":1,"textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0}}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"countdown":{"countdownDays":30}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "做一张春节倒计时卡片，显示距离2027年2月6日春节还有多少天。本轮卡片静态内容（用作展示的外部事实）：2027年春节是2月6日。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "countdown": {
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
      "id": "photo-ux-texture-orange-diamond-square",
      "src": "https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/833c5de3326049de993cc193a526df84/cbfe92acc718409aae519be674465497.jpg",
      "description": "主题背景"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetCountdownDays"
  ],
  "event": [],
  "asset": [
    "photo-ux-texture-orange-diamond-square"
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
        "targetDate": "2027-02-06"
      },
      "writeResultTo": "/data/countdown",
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
  "artifactId": "611f9321-a215-468b-9757-ccb1295a5c7d",
  "createdAt": 1793541115976
}
```
```designcompactdsl
["root","Stack",{"width":160,"height":160,"padding":0,"borderRadius":18,"clip":true,"alignContent":"topStart","backgroundColor":"#00000000"},["__post_theme_background","template_root"]]
["__post_theme_background","Stack",{"width":"matchParent","height":"matchParent","alignContent":"topStart"},["__post_theme_base"]]
["__post_theme_base","Image",{"width":"matchParent","height":"matchParent","objectFit":"fill","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/833c5de3326049de993cc193a526df84/cbfe92acc718409aae519be674465497.jpg"}]
["template_root","Stack",{"width":"matchParent","height":"matchParent","padding":12},["__genui_render_component__template_root"]]
["__genui_render_component__template_root","Stack",{"width":"matchParent","height":"matchParent"},["root_1"]]
["root_1","Stack",{"width":"matchParent","height":"matchParent","alignContent":"topStart"},["root_1_0"]]
["root_1_0","Column",{"width":"matchParent","height":"matchParent","justifyContent":"spaceBetween","alignItems":"center","constraintSize":{"minWidth":0,"minHeight":0}},["root_1_0_0","root_1_0_1"]]
["root_1_0_0","Column",{"width":"matchParent","justifyContent":"start","alignItems":"center","constraintSize":{"minWidth":0,"minHeight":0}},["root_1_0_0_0","root_1_0_0_1"]]
["root_1_0_0_0","Text",{"width":"matchParent","height":24,"margin":{"top":4},"fontSize":12,"minFontSize":12,"fontWeight":500,"fontColor":"#CCFFFFFF","maxLines":1,"textAlign":"center","textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0},"content":"春节还剩"}]
["root_1_0_0_1","Text",{"height":58,"margin":{"top":8},"fontSize":48,"fontWeight":700,"fontColor":"#FFFFFFFF","maxLines":1,"textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0},"content":"{{ ${/data/countdown/countdownDays} }}"}]
["root_1_0_1","Text",{"height":16,"fontSize":12,"fontWeight":500,"fontColor":"#CCFFFFFF","maxLines":1,"textOverflow":"ellipsis","constraintSize":{"minWidth":0,"minHeight":0},"content":"天"}]
["/",{"data":{"countdown":{"countdownDays":30}}}]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMU-AL10 7.0.0.111",
    "candidateAssetIds": [],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "距离春节还有多少天",
    "userQuery": "做一张春节倒计时卡片，显示距离2027年2月6日春节还有多少天。本轮卡片静态内容（用作展示的外部事实）：2027年春节是2月6日。",
    "title": "春节倒计时",
    "candidateDataBindings": [
      {
        "arguments": {
          "targetDate": "2027-02-06"
        },
        "candidateOutputFields": [
          "/countdownDays"
        ],
        "capabilityId": "GetCountdownDays",
        "writeResultTo": "/data/countdown"
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMU-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101135153660"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "1",
    "isNew": false,
    "sessionId": "fe3b6587-7ed4-4876-a66e-d4b6576ded8f"
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
  "romVersion": "CMU-AL10 7.0.0.111",
  "candidateAssetIds": [],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "距离春节还有多少天",
  "userQuery": "做一张春节倒计时卡片，显示距离2027年2月6日春节还有多少天。本轮卡片静态内容（用作展示的外部事实）：2027年春节是2月6日。",
  "title": "春节倒计时",
  "candidateDataBindings": [
    {
      "arguments": {
        "targetDate": "2027-02-06"
      },
      "candidateOutputFields": [
        "/countdownDays"
      ],
      "capabilityId": "GetCountdownDays",
      "writeResultTo": "/data/countdown"
    }
  ]
}
```
