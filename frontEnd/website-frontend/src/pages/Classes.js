import React from 'react';
import "../App";
import classData from "../data/data.json";

function Classes(){
    return (
        <div classname = 'Classes'>
            <h1>Classes Num</h1>
            {classData.map((postDetail, index)=>{
                return <h1>{postDetail.containerName} - {postDetail.categoryName}({postDetail['date (DD-MM-YYYY)']}) - {postDetail.description}</h1>
            })}
        </div>
    )
}
export default Classes;