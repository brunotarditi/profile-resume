import { Routes, Route } from "react-router-dom";
import PersonalData from '../views/PersonalData';
import Experience from '../views/Experience';
const AppRouting = (props) => {
    return (
        <div>
            <Routes>
                <Route exact path="/profile-resume" element={<PersonalData open={props.open}/>} />
                <Route path="/experience" element={<Experience open={props.open}/>} />
            </Routes>
        </div>
    )
}

export default AppRouting
