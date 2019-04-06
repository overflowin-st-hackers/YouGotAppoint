import React,{Component} from 'react';
import key from "weak-key";
// import HomePage from './homepage';
// import DashBoard from './dashboard';

// let userData = {
//     isLoggedIn: false,
//     credentials: null,
//     // changeState: ()
// }

// let userContext = React.createContext(userData);

class ErrorBoundary extends Component{
    constructor(props)
    {
        super(props)
        this.state = {
            hasError: false
        }
    }
    static getDerivedStateFromError(error){
        return {hasError: true};
    }
    render(){
        if(this.state.hasError){
            <h1> Something Went Wrong</h1>
        }
        return this.props.children;
    }
}

class App extends Component{
    constructor(props)
    {
        super(props);
        this.state = {
            isLoading: true,
            placeHolder: 'Loading...'
        }
    }

    render(){
        // return (<userContext.Provider value={userData}> 
        //     {this.state.userLoggedIn? <HomePage/> : <DashBoard />}
        // </userContext.Provider>)
        return (<>
            {this.state.doctors===undefined?"No Data":this.state.doctors.map((doctor)=>(
                <div key={doctor.pk}> 
                    <p> Name: {doctor.name} </p>
                    <p> contact: {doctor.contact_no}</p>
                    <div> Specializations: <ul> {doctor.specializations.map((specialization)=>(<li key={key({spec: specialization})}> {specialization} </li>))} </ul> </div>
                    <p> Rating: {doctor.rating} </p>
                    <p> Degrees: {doctor.degrees} </p>
                    <p></p>
                </div>
        ))}
        </>)
    }

    componentDidMount(){
        fetch('/api/doctors/').then(response=>{
            if(response.status != 200)
                return this.setState({placeHolder: 'Something went wrong!'});
            return response.json();
        }).then(data=>{
            this.setState({
                doctors: data, 
                isLoading: false
            })
        })
    }
}

export default App;
export {ErrorBoundary};