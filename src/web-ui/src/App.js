import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

   // new line start
  const [playlist, setPlaylist] = useState(null)
  const [play, addP] = useState(" ");
  function getData(id) {
    const myID = id;
    axios({
      method: "GET",
      url:`/data?id=${myID}` ,
    })
    .then((response) => {
      const res =response.data
      setPlaylist(({
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
    function MyForm() {
      function handleSubmit(e) {
        // Prevent the browser from reloading the page
        e.preventDefault();
    
        // Read the form data
        const form = e.target;
        console.log(form)
        const formData = new FormData(form);
        const playlistID = formData.get("playlistID");
        console.log(playlistID)
        // You can pass formData as a fetch body directly:
        getData(playlistID)
    
      }
    
      return (
        <form method="post" onSubmit={handleSubmit}>
          <label>
            Playlist ID: <input name="playlistID"  />
          </label>
          <hr />
  
        
          <button type="submit">Submit form</button>
        </form>
      );
    }
    function addPlaylist()
    {
      console.log("HERE");
      function handleSubmit(e)
      {
        e.preventDefault();
    
        // Read the form data
        const form = e.target;
        const formData = new FormData(form);
        // console.log(formData)
        const add = formData.get('value');
        console.log(add)
        // You can pass formData as a fetch body directly:
        if(add =="yes")
        {
          submitPlaylist(add)
        }
        
        
    
      }
      return (
        <form>
        <select value={play} onSubmit={handleSubmit}>
          <option value="yes">Yes</option>
          <option value="no">No</option>
          
        </select>
        <button type="submit">Submit</button>
      </form>
      )
    }
    function submitPlaylist()
    {

      axios({
        method: "GET",
        url:`/build` ,
      })
      
    }
  return (
    <div className="App">
      <header className="App-header">
        
        <p>
         Enter Playlist Link to get Reccomended songs!
        </p>
       

        {/* new line start*/}
        <p>To get your new songs {MyForm()}</p>
        {playlist && <div>
          <ul  style={{ listStyleType: 'none' }}>
  {/* List items */}

        {playlist.new_songs.map((song, index) => (
          <li key={index}>{song}</li>
        ))}
      </ul>
          
            </div>
           
        }
       
         {/* end of new line */}
        
      </header>
      {/* <div className='body'> <p> {addPlaylist()}</p></div> */}
    </div>
  );
}

export default App;