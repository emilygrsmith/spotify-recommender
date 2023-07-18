import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    const myID = '6kEqWqF4dSacolt357S2nE';
    axios({
      method: "GET",
      url:`/data?id=${myID}` ,
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        new_songs: res
        
       }))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <header className="App-header">
        
        <p>
         Enter Playlist ID to get Reccomended songs!
        </p>
       

        {/* new line start*/}
        <p>To get your new songs </p><button onClick={getData}>Click me</button>
        {profileData && <div>
          <ul>
        {profileData.new_songs.map((song, index) => (
          <li key={index}>{song}</li>
        ))}
      </ul>
          
            </div>
        }
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;