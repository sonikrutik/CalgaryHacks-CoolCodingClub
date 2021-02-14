import React from 'react'
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";


export const SidebarData = [
    {
        title: "HOME",
        path: "/",
        icon: <AiIcons.AiFillHome/>,
        cName:'nav-text'
    },
    {
        title: "CLASSES",
        path: "/classes",
        icon: <FaIcons.FaSchool/>,
        cName:'nav-text'
    },
    {
        title: "PROGRESS",
        path: "/progress",
        icon: <AiIcons.AiOutlineBarChart/>,
        cName:'nav-text'
    },

]