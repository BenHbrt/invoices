import axios from 'axios';

import { useContext, useState } from 'react';
import { UserContext } from '../App';
import { urlBase } from '../data/urls';



const LoginPage = () => {

    const { user, setUser } = useContext(UserContext);

    const [loginData, setLoginData] = useState({username: "", password: ""});

    const handleChange = (e) => {
        const newData = { ...loginData };
        newData[e.target.name] = e.target.value;
        setLoginData(newData);
    }

    const handleSubmit = async () => {
        try {
            const response = await axios.post(`${urlBase}auth/token/login/`, loginData);
            const token = response.data.auth_token;
            console.log(token)

            try {
                const response = await axios.get(`${urlBase}auth/users/me/`, {headers: {'Authorization': 'Token ' + token}});
                const userData = response.data;
                setUser({username: userData.username, id: userData.id, token: token});
            } catch (error) {
                console.error(error)
            }

        }
        catch (error) {
            console.error(error)
        }
    }

    return (
        <main>
            <input type="text" value={loginData.username} name="username" onChange={(e) => handleChange(e)} />
            <input type="password" value={loginData.password} name="password" onChange={(e) => handleChange(e)}/>
            <button onClick={handleSubmit}>Login</button>
        </main>
    );
};

export default LoginPage;