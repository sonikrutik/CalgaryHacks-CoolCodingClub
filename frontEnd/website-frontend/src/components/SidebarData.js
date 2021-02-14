import React from 'react'
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import AllInboxIcon from '@material-ui/icons/AllInbox';
import DateRangeIcon from '@material-ui/icons/DateRange';
import TodayIcon from '@material-ui/icons/Today';
import SchoolIcon from '@material-ui/icons/School';

export const SidebarData = [
    {
        title: "HOME",
        path: "/",
        icon: <AiIcons.AiFillHome/>,
        cName:'nav-text'
    },
    {
        title: "INBOX",
        path: "/Inbox",
        icon: <AllInboxIcon/>,
        cName:'nav-text'
    },
    {
        title: "TODAY",
        path: "/Today",
        icon: <TodayIcon/>,
        cName:'nav-text'
    },
    {
        title: "NEXT 7 DAYS",
        path: "/Week",
        icon: <DateRangeIcon/>,
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