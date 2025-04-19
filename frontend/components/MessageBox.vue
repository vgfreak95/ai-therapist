<template>
  <div class="message-box">
    <span class="message-text">{{ messageContent }}</span>
    <div class="lower-message-box">
      <button class="btn-message-box">
        <i class="bi bi-volume-up"></i>
        <span>Voice</span>
      </button>
    </div>
  </div>
</template>


<script>
import Chatbox from '../components/Chatbox.vue'

export default {
  name: "MessageBox",
  props: {
    messageContent: {
      type: String,
      required: true
    },

  },

}
</script>

<style>
/* default chat message */
.message-box {
  width: auto;
  height: auto;
  padding: 10px;
  font-size: 28px;
  background-color: white;
  border-color: black;
  border-radius: 20px;
  border: 3px solid black;
  background-color: rgba(255, 209, 248, 0.88);
  overflow-y: auto;
  min-height: 20px;
  max-height: 400px;
  min-width: 50px;
  max-width: 500px;
  resize: none;
  margin-bottom: 30px;
}

/* align chat to left */
.message-box.left {
  margin-right: auto;
  margin-left: 10px;
}

/* align chat to right */
.message-box.right {
  margin-left: auto;
  margin-right: 10px;
  background-color: rgb(79, 195, 247)
}

.lower-message-box {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

.btn-message-box {
  display: flex;
  align-items: center;
  gap: 5px;
  background-color: antiquewhite;
  margin-top: 20px;
  font-size: 25px;
  padding: 5px 10px;
  border: 3px solid black;
  border-radius: 0px 0px 10px 10px;
  cursor: pointer;
}

.btn-message-box::hover {
  color: green;
}

.bi.bi-volume-up {
  justify-content: center;
  font-size: 35px;
}
</style>
