import React from 'react';
import Post from './Post';

const Posts = (props) => (
  <div className='posts'>
    {
      props.posts.map((post) => (
        <Post
          key={post.name}
          postName={post.name}
          postAddress={post.address}
          postEntry={post.entry}
        />
      ))
  }
  </div>
);

export default Posts;