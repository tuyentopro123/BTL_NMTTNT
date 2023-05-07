import React, { useCallback, useState } from "react";
import "./Chart.css"
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend, Sector, LabelList, Label } from 'recharts';
import { scaleOrdinal } from 'd3-scale';
import { schemeCategory10 } from 'd3-scale-chromatic';


const RADIAN = Math.PI / 180;
const renderCustomizedLabel = (props) => {
    const {
        cx,
        cy,
        midAngle,
        innerRadius,
        outerRadius,
        percent,
    } = props;
    const sin = Math.sin(-RADIAN * midAngle);
    const cos = Math.cos(-RADIAN * midAngle);
    const radius = innerRadius + (outerRadius - innerRadius) * 0.75;

    const ex = (cx + radius * cos) + (cos < 0 ? 1 : -1) * 7;
    const ey = cy + radius * sin;
    return (
        <g>
            <text
                x={ex + (cos < 0 ? 1 : -1) * 15}
                y={ey}
                textAnchor={cos >= 0 ? "start" : "end"}
                fill="black"
                style={{fontSize: "10px"}}
            >
                {`${(percent).toFixed(2)}%`}
            </text>
        </g>
    );
};
const Chart = ({ data }) => {
    const CustomPieChartLabel = React.memo(renderCustomizedLabel);
    // const COLOR_COUNT = 10;
    // const colorScale = scaleOrdinal(schemeCategory10);

    // const COLORS = [];
    // for (let i = 0; i < COLOR_COUNT; i++) {
    //     COLORS.push(colorScale(i));
    // }
    
    const COLORS = [
        '#7AD6FF', '#FEB57E', '#FEDB75', '#FEF67A', '#DAFC81', '#87FC77',
        '#83F7A2', '#79FCD0', '#7EFEE5', '#ec9aff','#79FCFF'
    ];

    const LIMIT = 10; // số phần tử giới hạn là 9

    // tính tổng percent của các phần tử từ vị trí thứ 9 trở đi
    const totalPercent = data.slice(LIMIT).reduce((sum, item) => sum + item.percent, 0);
    const totalQuantity = data.slice(LIMIT).reduce((sum, item) => sum + item.quantity, 0);

    // tạo mảng mới
    const newData = [
    ...data.slice(0, LIMIT), // 9 phần tử đầu tiên
    { name: "khác", percent: totalPercent, quantity: totalQuantity } // phần tử thứ 10
    ];


    const formatTooltip = (value, name, props) => {
        console.log(value, name, props);
        const percent = parseFloat(value).toFixed(2);
        return `${props.payload.quantity} (${percent}%)`;
      };
    return (
        <div style={{ width: '80%',height: "500px" }} className={"chart-height"}>
            {
                data && data.length ?
                    <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                            <Tooltip formatter={formatTooltip} />
                            <Legend layout="vertical" />
                            <Pie
                                data={newData.map(obj => ({
                                    ...obj,
                                    percent: parseFloat(obj.percent.toFixed(2)),
                                  }))}
                                cx="50%"
                                cy="40%"
                                labelLine={false}
                                // label={<CustomPieChartLabel />}
                                startAngle={-270}
                                outerRadius={100}
                                fill="#8884d8"
                                dataKey="percent"
                                nameKey="name"
                            >
                                {data.map((entry, index) => (
                                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                ))}
                            </Pie>
                        </PieChart>
                    </ResponsiveContainer>
                    :
                    <div></div>
            }
        </div>
    )
}
export default Chart;