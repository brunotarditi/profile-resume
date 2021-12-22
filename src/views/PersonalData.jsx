import { Grid } from '@mui/material';
import ProfileCard from '../components/ProfileCard';
import photo from '../assets/img/photo.png'
import data from '../data/profile.json';

const PersonalData = () => {
    const profile = data.map((value) => {
        const dateNow = new Date();
        const age = dateNow.getUTCFullYear() - value.personal.date.split('/')[2];
        return (
            <ProfileCard
                key={value.id}
                fullname={value.personal.first_name + " " + value.personal.last_name}
                photo={photo}
                age={age}
                date={value.personal.date}
            />
        )
    })
    return (
        <Grid container >
            <Grid item xs={12} sm={6}>
                {profile}
            </Grid>
        </Grid>
    )
}

export default PersonalData
