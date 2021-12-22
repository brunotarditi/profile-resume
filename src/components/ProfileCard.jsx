import React from 'react'
import { Typography, Card, CardMedia, CardContent, CardActions, Button } from '@mui/material';


const ProfileCard = (props) => {
    return (
        <div>
            <Card sx={{ maxWidth: 800, width:400 }}>
                <CardMedia
                    component="img"
                    height="350"
                    image={props.photo}
                    alt="profile"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        {props.fullname}
                    </Typography>
                    <Typography variant="body1" color="text.secondary">
                        Fecha de nacimiento {props.date + "\n"} 
                        Edad {props.age}.
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small">Share</Button>
                    <Button size="small">Learn More</Button>
                </CardActions>
            </Card>
        </div>
    )
}

export default ProfileCard
