```cardspec
{
  "title": "照片备份倒计时",
  "description": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetDateCounter",
      "arguments": {
        "targetDate": "2026-07-01",
        "repeat": {
          "unit": "month",
          "interval": 2
        }
      },
      "writeResultTo": "/data/dateCounter"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["__post_theme_background","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#FF1F1F99"}},{"id":"__post_theme_background","component":"Stack","children":["fusionBallBackground","__post_theme_base"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"__post_theme_base","component":"Image","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/4763de2ea917462b824e2383a5154130/edb07e0ba593472ab9c27d61efeb40fe.jpg","styles":{"width":"matchParent","height":"matchParent","objectFit":"fill"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F1F99","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF2B65D9","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF57AED9","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"照片备份","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#CCFFFFFF"}},{"id":"title_icon","component":"Image","src":"resources/base/media/stopwatch_fill.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FFFFFFFF"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/dateCounter/relationText} + ' ' + ${/data/dateCounter/days} + ' 天' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"下次备份","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99FFFFFF","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/dateCounter/targetDateText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FFFFFFFF","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"dateCounter":{"days":3,"relationText":"还剩","targetDateText":"2026/11/09"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
  "size": "2x2",
  "appVersion": "11.9.9.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "dateCounter": {
        "days": {
          "type": "integer",
          "description": "今天与本次实际目标日期之间的非负自然日天数，不包含单位。大于0时可搭配relationText和“天”展示；等于0时仅展示relationText。",
          "sampleValue": 3
        },
        "relationText": {
          "type": "string",
          "description": "枚举字符串：['还剩','已过','就是今天']。根据当前日期与目标日期的关系，返回一个关联文本，便于直接拼接展示。例如与倒计时事件名称拼接：{'xx事件 '+{relationText}}作为标题，显示为“xx事件 还剩”。",
          "sampleValue": "还剩"
        },
        "targetDateText": {
          "type": "string",
          "description": "本次实际目标的公历日期，格式为YYYY/MM/DD。单次计时返回目标日期对应的公历日期；周期计时返回本次选中的周期日期对应的公历日期。",
          "sampleValue": "2026/11/09"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.stopwatch_fill",
      "src": "resources/base/media/stopwatch_fill.svg",
      "description": "样式：默认黑色的单色秒表实心图标，内部通过镂空表现表盘指针，支持通过 fillColor 与卡片配色统一；适用：计时功能、运动计时、倒计时。"
    },
    {
      "id": "asset.calendar_fill",
      "src": "resources/base/media/calendar_fill.svg",
      "description": "样式：日历实心图标，默认黑色，图形为带格线的日历本造型；适用：日程管理、日历事件查看、当日安排。"
    },
    {
      "id": "photo-ux-texture-blue-diagonal-square",
      "src": "https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/4763de2ea917462b824e2383a5154130/edb07e0ba593472ab9c27d61efeb40fe.jpg",
      "description": "主题背景"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetDateCounter"
  ],
  "event": [],
  "asset": [
    "asset.stopwatch_fill",
    "asset.calendar_fill",
    "photo-ux-texture-blue-diagonal-square"
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
      "capabilityId": "GetDateCounter",
      "arguments": {
        "targetDate": "2026-07-01",
        "repeat": {
          "unit": "month",
          "interval": 2
        }
      },
      "writeResultTo": "/data/dateCounter",
      "candidateOutputFields": [
        "/days",
        "/relationText",
        "/targetDateText"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.stopwatch_fill",
    "asset.calendar_fill"
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
  "artifactId": "5a01dc50-270e-4457-a46f-dc921c0539a5",
  "createdAt": 1794227106164
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":"照片备份","icon":"resources/base/media/stopwatch_fill.svg","fontSize":12}]
["primary","EmphasisText",{"mainText":"{{ ${/data/dateCounter/relationText} + ' ' + ${/data/dateCounter/days} + ' 天' }}","fontSize":18}]
["support","SecondaryBody",{"items":[{"label":"下次备份 ","value":{"path":"/data/dateCounter/targetDateText"}}],"fontSize":14}]
["/data/dateCounter/days",3]
["/data/dateCounter/relationText","还剩"]
["/data/dateCounter/targetDateText","2026/11/09"]
```
```request
{
  "content": {
    "bundleName": "com.omega_w_0823.hmservice",
    "userQuery": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
    "candidateDataBindings": [
      {
        "capabilityId": "GetDateCounter",
        "arguments": {
          "targetDate": "2026-07-01",
          "repeat": {
            "unit": "month",
            "interval": 2
          }
        },
        "writeResultTo": "/data/dateCounter",
        "candidateOutputFields": [
          "/days",
          "/relationText",
          "/targetDateText"
        ]
      }
    ],
    "title": "照片备份倒计时",
    "size": "2x2",
    "candidateEventCandidates": [],
    "description": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
    "candidateAssetIds": [
      "asset.stopwatch_fill",
      "asset.calendar_fill"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "SGT-AL10",
    "prdVer": "11.9.9.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261103090000000"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q086-000",
    "isNew": true,
    "sessionId": "batch-615f11cd"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
    "type": "text"
  },
  "version": "1.0",
  "bundleName": "com.omega_w_0823.hmservice",
  "userQuery": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
  "candidateDataBindings": [
    {
      "capabilityId": "GetDateCounter",
      "arguments": {
        "targetDate": "2026-07-01",
        "repeat": {
          "unit": "month",
          "interval": 2
        }
      },
      "writeResultTo": "/data/dateCounter",
      "candidateOutputFields": [
        "/days",
        "/relationText",
        "/targetDateText"
      ]
    }
  ],
  "title": "照片备份倒计时",
  "size": "2x2",
  "candidateEventCandidates": [],
  "description": "从2026年7月1日起每两个月备份一次照片，桌面上显示距下次还有几天。",
  "candidateAssetIds": [
    "asset.stopwatch_fill",
    "asset.calendar_fill"
  ]
}
```
