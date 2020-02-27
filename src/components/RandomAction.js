import React from 'react';

const RandomAction = (props) => (
  <div>
    <button
      className='button big-button'
      onClick={props.handlePick}
    >
      Random Post
    </button>
  </div>
);

export default RandomAction;