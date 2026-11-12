```cardspec
{
  "title": "我的记忆",
  "description": "笔记与待办速览",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["first","second"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":8,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"first","component":"Column","children":["first_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"first_text","component":"Column","children":["first_primary_row","first_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"first_primary_row","component":"Row","children":["first_primary_value","first_primary_unit"],"itemMargin":2,"styles":{"height":22,"alignItems":"bottom","flexShrink":0}},{"id":"first_primary_value","component":"Text","content":"{{ ${/data/memo/noteCount} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"first_primary_unit","component":"Text","content":"条","styles":{"height":16.0,"fontSize":10,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","padding":{"top":0,"right":0,"bottom":2,"left":0},"textOverflow":"clip"}},{"id":"first_secondary","component":"Text","content":"备忘录笔记","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#991F4799"}},{"id":"second","component":"Column","children":["second_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":63,"backgroundColor":"#CCFFFFFF","layoutWeight":1}},{"id":"second_text","component":"Column","children":["second_primary_row","second_secondary"],"itemMargin":0,"styles":{"alignItems":"start","justifyContent":"center","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"second_primary_row","component":"Row","children":["second_primary_value","second_primary_unit"],"itemMargin":2,"styles":{"height":22,"alignItems":"bottom","flexShrink":0}},{"id":"second_primary_value","component":"Text","content":"{{ ${/data/memo/todoTotalCount} }}","styles":{"height":22,"fontSize":16,"fontWeight":700,"maxLines":1,"flexShrink":1,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"second_primary_unit","component":"Text","content":"条","styles":{"height":16.0,"fontSize":10,"fontWeight":500,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","padding":{"top":0,"right":0,"bottom":2,"left":0},"textOverflow":"clip"}},{"id":"second_secondary","component":"Text","content":"{{ '待办 未完成' + ${/data/memo/todoPendingCount} + ' 已完成' + ${/data/memo/todoCompletedCount} }}","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"memo":{"noteCount":0,"todoTotalCount":0,"todoPendingCount":0,"todoCompletedCount":0}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一个我的记忆卡片，展示我的备忘录笔记和待办信息",
  "size": "2x2",
  "appVersion": "11.7.9.300",
  "eventCandidates": [
    {
      "id": "event.viewNote",
      "description": "打开华为备忘录应用。",
      "call": "clickToIntent",
      "args": {
        "abilityName": "MainAbility",
        "bundleName": "com.huawei.hmos.notepad",
        "intentName": "ViewNote",
        "params": {
          "launchSource": "1",
          "launchType": "0"
        }
      }
    }
  ],
  "dataModelSchema": {
    "data": {
      "memo": {
        "noteCount": {
          "type": "integer",
          "description": "查询到的笔记总数量（已过滤已删除笔记）。",
          "sampleValue": 0
        },
        "favoriteNoteCount": {
          "type": "integer",
          "description": "收藏笔记数。",
          "sampleValue": 0
        },
        "notes": [
          {
            "title": {
              "type": "string",
              "description": "笔记标题，若无标题则回退为'无标题'。",
              "sampleValue": "示例"
            }
          }
        ],
        "todoTotalCount": {
          "type": "integer",
          "description": "查询到的待办总数量（已过滤已删除待办）。",
          "sampleValue": 0
        },
        "todoCompletedCount": {
          "type": "integer",
          "description": "已完成的待办记录数。",
          "sampleValue": 0
        },
        "todoPendingCount": {
          "type": "integer",
          "description": "未完成的待办记录数。",
          "sampleValue": 0
        },
        "todos": [
          {
            "title": {
              "type": "string",
              "description": "待办标题，若无标题则回退为'无标题'。",
              "sampleValue": "示例"
            }
          }
        ]
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.bell_fill",
      "src": "resources/base/media/bell_fill.svg",
      "description": "样式：默认黑色的单色实心铃铛图标，采用经典吊铃造型，底部带铃舌，原始尺寸为 24×24；适用：通知提醒、消息提示、备忘录提醒、闹钟响铃或开启状态，以及日历事项提醒。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetMemoData"
  ],
  "event": [
    {
      "id": "event.viewNote",
      "description": "打开华为备忘录应用。",
      "call": "clickToIntent",
      "args": {
        "abilityName": "MainAbility",
        "bundleName": "com.huawei.hmos.notepad",
        "intentName": "ViewNote",
        "params": {
          "launchSource": "1",
          "launchType": "0"
        }
      }
    }
  ],
  "asset": [
    "asset.bell_fill"
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
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo",
      "candidateOutputFields": [
        "/noteCount",
        "/favoriteNoteCount",
        "/notes/0/title",
        "/todoTotalCount",
        "/todoCompletedCount",
        "/todoPendingCount",
        "/todos/0/title"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.viewNote",
      "action": {
        "call": "clickToIntent",
        "args": {
          "abilityName": "MainAbility",
          "bundleName": "com.huawei.hmos.notepad",
          "intentName": "ViewNote",
          "params": {
            "launchSource": "1",
            "launchType": "0"
          }
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.bell_fill"
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
  "artifactId": "267686d0-7c09-4695-b0be-214acf7f8487",
  "createdAt": 1793952166663
}
```
```designcompactdsl
["root","Layout",{"layout":"S-dual-info"},["first","second"]]
["first","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/memo/noteCount"},"secondaryText":"备忘录笔记","unit":"条"}]
["second","InfoBlock",{"surfaceRole":"panel","primaryText":{"path":"/data/memo/todoTotalCount"},"secondaryText":"{{ '待办 未完成' + ${/data/memo/todoPendingCount} + ' 已完成' + ${/data/memo/todoCompletedCount} }}","unit":"条"}]
["/data/memo/noteCount",0]
["/data/memo/todoTotalCount",0]
["/data/memo/todoPendingCount",0]
["/data/memo/todoCompletedCount",0]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.120",
    "candidateAssetIds": [
      "asset.bell_fill"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.viewNote",
        "action": {
          "call": "clickToIntent",
          "args": {
            "abilityName": "MainAbility",
            "bundleName": "com.huawei.hmos.notepad",
            "intentName": "ViewNote",
            "params": {
              "launchSource": "1",
              "launchType": "0"
            }
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "笔记与待办速览",
    "userQuery": "生成一个我的记忆卡片，展示我的备忘录笔记和待办信息",
    "title": "我的记忆",
    "candidateDataBindings": [
      {
        "capabilityId": "GetMemoData",
        "arguments": {},
        "writeResultTo": "/data/memo",
        "candidateOutputFields": [
          "/noteCount",
          "/favoriteNoteCount",
          "/notes/0/title",
          "/todoTotalCount",
          "/todoCompletedCount",
          "/todoPendingCount",
          "/todos/0/title"
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
    "time": "20261104065531527"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q439-000",
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
  "romVersion": "CMS-AL20 7.0.0.120",
  "candidateAssetIds": [
    "asset.bell_fill"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.viewNote",
      "action": {
        "call": "clickToIntent",
        "args": {
          "abilityName": "MainAbility",
          "bundleName": "com.huawei.hmos.notepad",
          "intentName": "ViewNote",
          "params": {
            "launchSource": "1",
            "launchType": "0"
          }
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "笔记与待办速览",
  "userQuery": "生成一个我的记忆卡片，展示我的备忘录笔记和待办信息",
  "title": "我的记忆",
  "candidateDataBindings": [
    {
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo",
      "candidateOutputFields": [
        "/noteCount",
        "/favoriteNoteCount",
        "/notes/0/title",
        "/todoTotalCount",
        "/todoCompletedCount",
        "/todoPendingCount",
        "/todos/0/title"
      ]
    }
  ]
}
```
