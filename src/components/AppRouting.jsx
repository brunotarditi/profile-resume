import React from 'react'
import { Routes, Route } from "react-router-dom";
import Main from './Main';
import Experience from './Experience';
const AppRouting = () => {
    return (
        <div>
            <Routes>
                <Route exact path="/profile-resume" element={<Main />} />
                <Route path="/profile-resume/experience" element={<Experience/>} />
            </Routes>
        </div>
    )
}

export default AppRouting
