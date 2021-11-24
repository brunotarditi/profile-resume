import { Routes, Route } from "react-router-dom";
import PersonalData from '../components/PersonalData';
import Experience from '../components/Experience';
const AppRouting = (props) => {
    return (
        <div>
            <Routes>
                <Route exact path="/profile-resume" element={<PersonalData open={props.open}/>} />
                <Route path="/experience" element={<Experience/>} />
            </Routes>
        </div>
    )
}

export default AppRouting
