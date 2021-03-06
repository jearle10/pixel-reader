import React from 'react';

function App() {
  return (
    <div class="container">

      <div class="row">
        <h4 class="center-align"> Upload an image of a card</h4>
        <form class="col s6 offset-s3" action="/predict" method="POST" enctype="multipart/form-data">
          <div class="file-field input-field">
            <div class="btn">
              <span>File</span>
              <input type="file" name="file"></input>
            </div>
            <div class="file-path-wrapper">
              <input class="file-path validate" type="text"></input>
            </div>
          </div>
          <button class="btn waves-effect waves-light" type="submit" name="action">Submit
                  <i class="material-icons right">send</i>
          </button>
        </form>
      </div>

    </div>
  );
}

export default App;
