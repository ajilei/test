const button = [
    { text: '新建客户', type: 'submit' },
    { text: '新建任务', type: 'submit' },
    { text: '新建工单', type: 'submit' },
    { text: '转移客户', type: 'submit' },
    { text: '导入数据', type: 'submit' },
    { text: '导出数据', type: 'submit' },
];

const table_1 = ['编号', '公司名', '客户状态','操作'];
const data_1 = [
    [1, '公司a', '正常','删除'],
    [2, '公司b', '正常','删除']
];

function init_table() {
    const targetDiv = document.getElementById('table_1');

    // 创建表格
    const table = document.createElement('table');
    table.classList.add('table', 'table-bordered', 'table-hover', 'table-striped');

    // 创建表头
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    table_1.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // 创建data
    const tbody = document.createElement('tbody');
    data_1.forEach(rowData => {
        const row = document.createElement('tr');
        rowData.forEach(cellData => {
            const cell = document.createElement('td');
            cell.textContent = cellData;
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    });
    table.appendChild(tbody);

    if (targetDiv) {
        targetDiv.appendChild(table);
    } else {
        console.error('无法找到ID为table_1的元素。');
    }
}

function init_button() {
    document.addEventListener("DOMContentLoaded", function() {
        const divBt1 = document.getElementById("bt-1");
        if (divBt1) {
            const hr = document.createElement("hr");
            hr.className = "mt5 mb15";
            divBt1.appendChild(hr);

            button.forEach(function(item) {
                const buttonText = item.text;
                const buttonType = item.type;
                const button = document.createElement("button");
                button.type = buttonType;
                button.className = "king-btn king-info";
                button.textContent = buttonText;
                // button.onclick = function() {}; // 点击事件处理函数
                divBt1.appendChild(button);
            });
        } else {
            console.error('无法找到ID为bt-1的元素。');
        }
    });
}

init_button();
init_table();
