```cardspec
{
  "title": "备忘录",
  "description": "备忘录速览",
  "suggestSize": "2x4",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["left","right"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"left","component":"Column","children":["__layout__left__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__left__sub","component":"Column","children":["left_title","__layout__left__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"left_title","component":"Row","children":["left_title_title","left_title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"left_title_title","component":"Text","content":"备忘录","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"left_title_icon","component":"Image","src":"resources/base/media/list_book_fill.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF1F4799"}},{"id":"__layout__left__body","component":"Column","children":["__layout__left__primary","__layout__left__details"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__left__primary","component":"Column","children":["left_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"left_primary","component":"Row","children":["left_primary_value","left_primary_unit"],"itemMargin":2,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"left_primary_value","component":"Text","content":"{{ ${/data/memo/noteCount} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"left_primary_unit","component":"Text","content":"篇","styles":{"height":17.0,"fontSize":12,"fontWeight":500,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","padding":{"top":0,"right":0,"bottom":5,"left":0},"textOverflow":"clip"}},{"id":"__layout__left__details","component":"Column","children":["left_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"left_support","component":"Column","children":["left_support_row0","left_support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"left_support_item0_label","component":"Text","content":"笔记","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"left_support_item0_value","component":"Text","content":"{{ ${/data/memo/notes/0/title} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"left_support_item0","component":"Row","children":["left_support_item0_label","left_support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"left_support_row0","component":"Row","children":["left_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"left_support_item1_label","component":"Text","content":"笔记","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"left_support_item1_value","component":"Text","content":"{{ ${/data/memo/notes/1/title} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"left_support_item1","component":"Row","children":["left_support_item1_label","left_support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"left_support_row1","component":"Row","children":["left_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"right","component":"Column","children":["__layout__right__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__right__sub","component":"Column","children":["right_title","__layout__right__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"right_title","component":"Row","children":["right_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"right_title_title","component":"Text","content":"待办","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__right__body","component":"Column","children":["__layout__right__primary","__layout__right__details"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__right__primary","component":"Column","children":["right_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"right_primary","component":"Row","children":["right_primary_value","right_primary_unit"],"itemMargin":2,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"right_primary_value","component":"Text","content":"{{ ${/data/memo/todoTotalCount} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"right_primary_unit","component":"Text","content":"项","styles":{"height":17.0,"fontSize":12,"fontWeight":500,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#991F4799","padding":{"top":0,"right":0,"bottom":5,"left":0},"textOverflow":"clip"}},{"id":"__layout__right__details","component":"Column","children":["right_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"right_support","component":"Column","children":["right_support_row0","right_support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"right_support_item0_value","component":"Text","content":"{{ ${/data/memo/todos/0/title} + ' · ' + (${/data/memo/todos/0/isComplete} ? '已完成' : '未完成') }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item0","component":"Row","children":["right_support_item0_value"],"itemMargin":0,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row0","component":"Row","children":["right_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"right_support_item1_value","component":"Text","content":"{{ ${/data/memo/todos/1/title} + ' · ' + (${/data/memo/todos/1/isComplete} ? '已完成' : '未完成') }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item1","component":"Row","children":["right_support_item1_value"],"itemMargin":0,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row1","component":"Row","children":["right_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"memo":{"noteCount":0,"notes":[{"title":"示例"},{"title":"示例"}],"todoTotalCount":0,"todos":[{"title":"示例","isComplete":false},{"title":"示例","isComplete":false}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在手机主屏幕放一个可视化备忘录卡片，展示备忘录笔记和待办事项的汇总信息，包括笔记总数、最近笔记列表、待办总数及待办明细。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
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
            },
            "content": {
              "type": "string",
              "description": "笔记正文（可截断），若无正文则为空字符串。",
              "sampleValue": "示例"
            },
            "modifiedTimeText": {
              "type": "string",
              "description": "修改时间格式化文本，格式为 'MM/DD HH:mm'，如 '07/16 14:35'。",
              "sampleValue": "示例"
            }
          },
          {
            "title": {
              "type": "string",
              "description": "笔记标题，若无标题则回退为'无标题'。",
              "sampleValue": "示例"
            },
            "content": {
              "type": "string",
              "description": "笔记正文（可截断），若无正文则为空字符串。",
              "sampleValue": "示例"
            },
            "modifiedTimeText": {
              "type": "string",
              "description": "修改时间格式化文本，格式为 'MM/DD HH:mm'，如 '07/16 14:35'。",
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
            },
            "isComplete": {
              "type": "boolean",
              "description": "该条待办是否已完成。true代表已完成，false代表未完成。",
              "sampleValue": false
            },
            "reminderTimeText": {
              "type": "string",
              "description": "提醒时间格式化文本，格式为 'HH:mm'，如 '14:30'；无提醒则显示 '--:--'。",
              "sampleValue": "示例"
            }
          },
          {
            "title": {
              "type": "string",
              "description": "待办标题，若无标题则回退为'无标题'。",
              "sampleValue": "示例"
            },
            "isComplete": {
              "type": "boolean",
              "description": "该条待办是否已完成。true代表已完成，false代表未完成。",
              "sampleValue": false
            },
            "reminderTimeText": {
              "type": "string",
              "description": "提醒时间格式化文本，格式为 'HH:mm'，如 '14:30'；无提醒则显示 '--:--'。",
              "sampleValue": "示例"
            }
          }
        ],
        "hasReminderToday": {
          "type": "boolean",
          "description": "今日是否存在未完成的提醒待办。true代表今日有提醒，false代表今日无提醒。",
          "sampleValue": false
        },
        "nextReminderTimeText": {
          "type": "string",
          "description": "最近一次未过期未完成提醒的格式化时间，格式为 'HH:mm'，如 '14:30'；无提醒则显示 '--:--'。",
          "sampleValue": "示例"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.list_book_fill",
      "src": "resources/base/media/list_book_fill.svg",
      "description": "样式：默认黑色的单色实心书册图标，内部带列表与文字线条，原始尺寸为 24×24；适用：目录、清单、记录册、备忘录列表、日程列表与健康记录列表。"
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
    "asset.list_book_fill"
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
        "/notes/0/content",
        "/notes/0/modifiedTimeText",
        "/notes/1/title",
        "/notes/1/content",
        "/notes/1/modifiedTimeText",
        "/todoTotalCount",
        "/todoCompletedCount",
        "/todoPendingCount",
        "/todos/0/title",
        "/todos/0/isComplete",
        "/todos/0/reminderTimeText",
        "/todos/1/title",
        "/todos/1/isComplete",
        "/todos/1/reminderTimeText",
        "/hasReminderToday",
        "/nextReminderTimeText"
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
    "asset.list_book_fill"
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
  "artifactId": "06e28e4d-17fd-4e54-b4c3-52fd04c29af5",
  "createdAt": 1793952232977
}
```
```designcompactdsl
["root","Layout",{"layout":"W-split-panels"},["left","right"]]
["left","Region",{"variant":"title-hero-support"},["left_title","left_primary","left_support"]]
["left_title","SingleLineTitle",{"title":"备忘录","icon":"resources/base/media/list_book_fill.svg","fontSize":12}]
["left_primary","EmphasizedData",{"value":{"path":"/data/memo/noteCount"},"unit":"篇","fontSize":30}]
["left_support","SecondaryBody",{"columns":1,"items":[{"label":"笔记 ","value":{"path":"/data/memo/notes/0/title"}},{"label":"笔记 ","value":{"path":"/data/memo/notes/1/title"}}],"fontSize":12}]
["right","Region",{"variant":"title-hero-support"},["right_title","right_primary","right_support"]]
["right_title","SingleLineTitle",{"title":"待办","fontSize":12}]
["right_primary","EmphasizedData",{"value":{"path":"/data/memo/todoTotalCount"},"unit":"项","fontSize":30}]
["right_support","SecondaryBody",{"columns":1,"items":[{"value":"{{ ${/data/memo/todos/0/title} + ' · ' + (${/data/memo/todos/0/isComplete} ? '已完成' : '未完成') }}"},{"value":"{{ ${/data/memo/todos/1/title} + ' · ' + (${/data/memo/todos/1/isComplete} ? '已完成' : '未完成') }}"}],"fontSize":12}]
["/data/memo/noteCount",0]
["/data/memo/notes/0/title","示例"]
["/data/memo/notes/1/title","示例"]
["/data/memo/todoTotalCount",0]
["/data/memo/todos/0/title","示例"]
["/data/memo/todos/0/isComplete",false]
["/data/memo/todos/1/title","示例"]
["/data/memo/todos/1/isComplete",false]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [
      "asset.list_book_fill"
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
    "description": "备忘录速览",
    "userQuery": "在手机主屏幕放一个可视化备忘录卡片，展示备忘录笔记和待办事项的汇总信息，包括笔记总数、最近笔记列表、待办总数及待办明细。",
    "title": "备忘录",
    "candidateDataBindings": [
      {
        "capabilityId": "GetMemoData",
        "arguments": {},
        "writeResultTo": "/data/memo",
        "candidateOutputFields": [
          "/noteCount",
          "/favoriteNoteCount",
          "/notes/0/title",
          "/notes/0/content",
          "/notes/0/modifiedTimeText",
          "/notes/1/title",
          "/notes/1/content",
          "/notes/1/modifiedTimeText",
          "/todoTotalCount",
          "/todoCompletedCount",
          "/todoPendingCount",
          "/todos/0/title",
          "/todos/0/isComplete",
          "/todos/0/reminderTimeText",
          "/todos/1/title",
          "/todos/1/isComplete",
          "/todos/1/reminderTimeText",
          "/hasReminderToday",
          "/nextReminderTimeText"
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
    "time": "20261102234735247"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q469-000",
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
    "asset.list_book_fill"
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
  "description": "备忘录速览",
  "userQuery": "在手机主屏幕放一个可视化备忘录卡片，展示备忘录笔记和待办事项的汇总信息，包括笔记总数、最近笔记列表、待办总数及待办明细。",
  "title": "备忘录",
  "candidateDataBindings": [
    {
      "capabilityId": "GetMemoData",
      "arguments": {},
      "writeResultTo": "/data/memo",
      "candidateOutputFields": [
        "/noteCount",
        "/favoriteNoteCount",
        "/notes/0/title",
        "/notes/0/content",
        "/notes/0/modifiedTimeText",
        "/notes/1/title",
        "/notes/1/content",
        "/notes/1/modifiedTimeText",
        "/todoTotalCount",
        "/todoCompletedCount",
        "/todoPendingCount",
        "/todos/0/title",
        "/todos/0/isComplete",
        "/todos/0/reminderTimeText",
        "/todos/1/title",
        "/todos/1/isComplete",
        "/todos/1/reminderTimeText",
        "/hasReminderToday",
        "/nextReminderTimeText"
      ]
    }
  ]
}
```
