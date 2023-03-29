import { createEntityAdapter } from "@reduxj/toolkit"

export const initialState = createEntityAdapter.getInitialState({
  id: null,
  video_title:'',
  user: null,
  description: '',
  likes: 0,
  dislikes: 0,
  video: null,
  rated: 0
})
