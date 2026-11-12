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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["content","__layout__root__slots"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"content","component":"Column","children":["__layout__content__sub"],"styles":{"height":"matchParent","layoutWeight":1},"itemMargin":0},{"id":"__layout__content__sub","component":"Column","children":["content_title","__layout__content__body"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":126.0}},{"id":"content_title","component":"Row","children":["content_title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"content_title_title","component":"Text","content":"备忘录","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__content__body","component":"Column","children":["content_body"],"itemMargin":0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1}},{"id":"content_body","component":"Column","children":["content_body_main","content_body_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_body_main","component":"Text","content":"{{ ${/data/memo/notes/0/title} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"content_body_secondary","component":"Text","content":"{{ ${/data/memo/notes/0/content} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__slots","component":"Column","children":["upper_region_shell","lower_region_shell"],"itemMargin":12,"styles":{"height":"matchParent","layoutWeight":1}},{"id":"upper","component":"Row","children":["upper_label","upper_visual"],"itemMargin":8,"onClick":[{"call":"clickToIntent","args":{"abilityName":"MainAbility","bundleName":"com.huawei.hmos.notepad","intentName":"ViewNote","params":{"launchSource":"1","launchType":"0"}}}],"styles":{"width":"matchParent","height":"matchParent","padding":{"left":12,"right":12,"top":7,"bottom":7},"borderRadius":16,"backgroundColor":"#99FFFFFF","alignItems":"center","justifyContent":"spaceBetween","flexShrink":0,"constraintSize":{"minWidth":0,"minHeight":48}}},{"id":"upper_label","component":"Text","content":"打开备忘录","styles":{"height":20,"fontSize":14,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1,"fontColor":"#FF1F4799"}},{"id":"upper_visual","component":"Image","src":"resources/base/media/list_book_fill.svg","styles":{"width":24,"height":24,"objectFit":"contain","flexShrink":0,"fillColor":"#FF1F4799"}},{"id":"lower","component":"Column","children":["lower_text"],"itemMargin":0,"styles":{"padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","clip":true,"flexShrink":0,"width":"matchParent","height":"matchParent","backgroundColor":"#99FFFFFF"}},{"id":"lower_text","component":"Column","children":["lower_primary","lower_secondary"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","flexShrink":1,"constraintSize":{"minWidth":0},"height":"matchParent","padding":{"top":8},"width":"matchParent"}},{"id":"lower_primary","component":"Text","content":"{{ ${/data/memo/notes/0/modifiedTimeText} }}","styles":{"height":19,"fontSize":14,"fontWeight":700,"maxLines":1,"flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3571428571428572,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"lower_secondary","component":"Text","content":"修改时间","styles":{"height":16,"fontSize":12,"fontWeight":500,"maxLines":1,"textOverflow":"ellipsis","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent","lineHeight":1.3333333333333333,"fontColor":"#991F4799"}},{"id":"upper_region_shell","component":"Column","children":["upper"],"itemMargin":0,"styles":{"layoutWeight":57.0,"width":"matchParent","alignItems":"start","justifyContent":"start"}},{"id":"lower_region_shell","component":"Column","children":["lower"],"itemMargin":0,"styles":{"layoutWeight":57.0,"width":"matchParent","alignItems":"start","justifyContent":"start"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"memo":{"notes":[{"title":"示例","content":"示例","modifiedTimeText":"示例"},{"title":"示例"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "在手机主屏幕生成一个备忘录卡片，展示备忘录笔记内容，点击卡片可跳转到备忘录应用进行编辑。",
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
  "artifactId": "a83d7454-124c-4787-a11f-ddcfc01681c5",
  "createdAt": 1793952230044
}
```
```designcompactdsl
["root","Layout",{"layout":"W-content-side-slots","orientation":"content-left"},["content","upper","lower"]]
["content","Region",{"variant":"title-content"},["content_title","content_body"]]
["content_title","SingleLineTitle",{"title":"备忘录","fontSize":12}]
["content_body","EmphasisText",{"mainText":{"path":"/data/memo/notes/0/title"},"secondaryText":{"path":"/data/memo/notes/0/content"},"fontSize":18}]
["upper","CardButton",{"label":"打开备忘录","icon":"resources/base/media/list_book_fill.svg","onClick":[{"call":"clickToIntent","args":{"abilityName":"MainAbility","bundleName":"com.huawei.hmos.notepad","intentName":"ViewNote","params":{"launchSource":"1","launchType":"0"}}}]}]
["lower","InfoBlock",{"variant":"slot","primaryText":{"path":"/data/memo/notes/0/modifiedTimeText"},"secondaryText":"修改时间"}]
["/data/memo/notes/0/title","示例"]
["/data/memo/notes/0/content","示例"]
["/data/memo/notes/0/modifiedTimeText","示例"]
["/data/memo/notes/1/title","示例"]
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
    "userQuery": "在手机主屏幕生成一个备忘录卡片，展示备忘录笔记内容，点击卡片可跳转到备忘录应用进行编辑。",
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
    "time": "20261103000016694"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q467-000",
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
  "userQuery": "在手机主屏幕生成一个备忘录卡片，展示备忘录笔记内容，点击卡片可跳转到备忘录应用进行编辑。",
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
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-content-side-slots\",\"orientation\":\"content-left\"},[\"content\",\"upper\",\"lower\"]]\n[\"content_title\",\"SingleLineTitle\",{\"title\":\"备忘录\",\"fontSize\":12}]\n[\"content_body\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/memo/notes/0/title\"},\"secondaryText\":{\"path\":\"/data/memo/notes/0/content\"},\"fontSize\":18}]\n[\"content\",\"Region\",{\"variant\":\"title-content\"},[\"content_title\",\"content_body\"]]\n[\"upper\",\"CardButton\",{\"label\":\"打开备忘录\",\"icon\":\"resources/base/media/list_book_fill.svg\",\"onClick\":[{\"call\":\"clickToIntent\",\"args\":{\"abilityName\":\"MainAbility\",\"bundleName\":\"com.huawei.hmos.notepad\",\"intentName\":\"ViewNote\",\"params\":{\"launchSource\":\"1\",\"launchType\":\"0\"}}}]}]\n[\"lower\",\"InfoBlock\",{\"variant\":\"slot\",\"primaryText\":{\"path\":\"/data/memo/notes/0/modifiedTimeText\"},\"secondaryText\":\"修改时间\"}]\n[\"/data/memo/notes/0/title\",\"示例\"]\n[\"/data/memo/notes/0/content\",\"示例\"]\n[\"/data/memo/notes/0/modifiedTimeText\",\"示例\"]\n[\"/data/memo/notes/1/title\",\"示例\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Row\",\"children\":[\"content\",\"__layout__root__slots\"],\"itemMargin\":12,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"content\",\"component\":\"Column\",\"children\":[\"__layout__content__sub\"],\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"__layout__content__sub\",\"component\":\"Column\",\"children\":[\"content_title\",\"__layout__content__body\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":126.0}},{\"id\":\"content_title\",\"component\":\"Row\",\"children\":[\"content_title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"content_title_title\",\"component\":\"Text\",\"content\":\"备忘录\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__content__body\",\"component\":\"Column\",\"children\":[\"content_body\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"end\",\"layoutWeight\":1}},{\"id\":\"content_body\",\"component\":\"Column\",\"children\":[\"content_body_main\",\"content_body_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"content_body_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/memo/notes/0/title} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"content_body_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/memo/notes/0/content} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__slots\",\"component\":\"Column\",\"children\":[\"upper_region_shell\",\"lower_region_shell\"],\"itemMargin\":12,\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1}},{\"id\":\"upper\",\"component\":\"Row\",\"children\":[\"upper_label\",\"upper_visual\"],\"itemMargin\":8,\"onClick\":[{\"call\":\"clickToIntent\",\"args\":{\"abilityName\":\"MainAbility\",\"bundleName\":\"com.huawei.hmos.notepad\",\"intentName\":\"ViewNote\",\"params\":{\"launchSource\":\"1\",\"launchType\":\"0\"}}}],\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":{\"left\":12,\"right\":12,\"top\":7,\"bottom\":7},\"borderRadius\":16,\"backgroundColor\":\"@theme:panel/1\",\"alignItems\":\"center\",\"justifyContent\":\"spaceBetween\",\"flexShrink\":0,\"constraintSize\":{\"minWidth\":0,\"minHeight\":48}}},{\"id\":\"upper_label\",\"component\":\"Text\",\"content\":\"打开备忘录\",\"styles\":{\"height\":20,\"fontSize\":14,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1,\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"upper_visual\",\"component\":\"Image\",\"src\":\"resources/base/media/list_book_fill.svg\",\"styles\":{\"width\":24,\"height\":24,\"objectFit\":\"contain\",\"flexShrink\":0,\"fillColor\":\"@theme:primary/1\"}},{\"id\":\"lower\",\"component\":\"Column\",\"children\":[\"lower_text\"],\"itemMargin\":0,\"styles\":{\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"clip\":true,\"flexShrink\":0,\"width\":\"matchParent\",\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\"}},{\"id\":\"lower_text\",\"component\":\"Column\",\"children\":[\"lower_primary\",\"lower_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"height\":\"matchParent\",\"padding\":{\"top\":8},\"width\":\"matchParent\"}},{\"id\":\"lower_primary\",\"component\":\"Text\",\"content\":\"{{ ${/data/memo/notes/0/modifiedTimeText} }}\",\"styles\":{\"height\":19,\"fontSize\":14,\"fontWeight\":700,\"maxLines\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3571428571428572,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"lower_secondary\",\"component\":\"Text\",\"content\":\"修改时间\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":500,\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\",\"lineHeight\":1.3333333333333333,\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"upper_region_shell\",\"component\":\"Column\",\"children\":[\"upper\"],\"itemMargin\":0,\"styles\":{\"layoutWeight\":57.0,\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"lower_region_shell\",\"component\":\"Column\",\"children\":[\"lower\"],\"itemMargin\":0,\"styles\":{\"layoutWeight\":57.0,\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"memo\":{\"notes\":[{\"title\":\"示例\",\"content\":\"示例\",\"modifiedTimeText\":\"示例\"},{\"title\":\"示例\"}]}}}}}",
  "validationErrors": []
}
```
