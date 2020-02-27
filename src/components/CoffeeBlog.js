const postsJson = require('./data/posts.json');
import React from 'react';
import Header from './Header';
import RandomAction from './RandomAction';
import Posts from './Posts'
import PostModal from './PostModal';

class CoffeeBlog extends React.Component {
  state = {
    posts: postsJson,
    selectedPost: undefined
  }
  handlePick = () => {
    const randomNum = Math.floor(Math.random() * this.state.posts.length);
    const selectedPost = this.state.posts[randomNum];
    this.setState(() => ({ selectedPost }));
  }
  handleClearSelectedPost = () => {
    this.setState(() => ({ selectedPost: undefined }))
  }
  render() {
    return (
      <div>
        <Header />
        <div className='container'>

          <RandomAction
            handlePick={this.handlePick}
          />
          <Posts
            posts={this.state.posts}
          />
          <PostModal
            selectedPost={this.state.selectedPost}
            handleClearSelectedPost={this.handleClearSelectedPost}
          />
        </div>
      </div>

    );

  }
}

export default CoffeeBlog;