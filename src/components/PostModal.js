import React from 'react';
import Modal from 'react-modal';

const PostModal = (props) => (
  <Modal
    appElement={document.getElementById('app')}
    isOpen={!!props.selectedPost}
    onRequestClose={props.handleClearSelectedPost}
    contentLabel='Selected Post'
    closeTimeoutMS={200}
    className='modal'
  >
    {props.selectedPost && <h2 className='modal__title'>{props.selectedPost.name}</h2>}
    {props.selectedPost && <h3 className='modal__subtitle'>{props.selectedPost.address}</h3>}
    {props.selectedPost && <p className='modal__body'>{props.selectedPost.entry}</p>}
    <button
      className='button'
      onClick={props.handleClearSelectedPost}
    >
      Close
    </button>
  </Modal>
);

export default PostModal;