const fs = require('fs');
// const keyword = process.argv[2];
// console.error(keyword);

async function query_result() {
    docx = "https://feishu.cn/drive/create/?type=docx"
    doc = "https://feishu.cn/drive/create/?type=doc"
    sheet = "https://feishu.cn/drive/create/?type=sheet"
    bitable = "https://feishu.cn/drive/create/?type=bitable"
    mindnote = "https://feishu.cn/drive/create/?type=mindnote"

    result_list = {
        // "doc":{'title': "新建文档",
        //        'subtitle': '' ,
        //        'valid': true,
        //        'arg': doc},
        "docx":{'title': "新建文档new",
                'subtitle': '' ,
                'valid': true,
                'arg': docx},
        "bitable":{'title': "新建多维表格",
                'subtitle': '' ,
                'valid': true,
                'arg': bitable},
        "sheet":{'title': "新建表格",
                'subtitle': '' ,
                'valid': true,
                'arg': sheet},
        "mindnote":{'title': "新建思维导图",
                'subtitle': '' ,
                'valid': true,
                'arg': mindnote}
    }
    const result_array = [];
    for (var key in result_list) {
        
        result_array.push(result_list[key])
    }
    console.log(JSON.stringify({ items: result_array }));
}
query_result();