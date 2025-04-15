<template>
  <div class="history">
    <div class="title">
      <label class="convo-title">Conversation</label>
    </div>
    <div class="conversation">
      <div v-for="msg in chatHistory" :class="['chat-message', msg.sender == 'therapist' ? 'left' : 'right']">
        {{ msg.message }}
      </div>
      <div class="footer">
        <Chatbox @message-sent="handleUserMessage" ref="chatbox" />
      </div>
    </div>
  </div>
</template>


<script>
import Chatbox from '../components/Chatbox.vue'


export default {
  name: "HistoryBox",

  data() {
    return {
      chatHistory: [],
      backendUrl: ''
    }
  },

  async mounted() {

    const config = useRuntimeConfig();
    this.backendUrl = config.public.backendUrl;

    this.chatHistory.push({ sender: "therapist", message: "..." });
    const stream = await this.$refs.chatbox.sendIntroduction(this.backendUrl);
    if (stream) {
      const lastIndex = this.chatHistory.length - 1;

      let streamMessage = "";
      await this.$refs.chatbox.streamMessage(stream, (chunk) => {
        streamMessage += chunk;
        this.chatHistory[lastIndex].message = streamMessage;
      });
    }
  },


  methods: {
    async handleUserMessage() {
      this.chatHistory.push({ sender: "user", message: this.$refs.chatbox.userInput });

      // Temp chat history for therapist
      this.chatHistory.push({ sender: "therapist", message: "..." });

      const stream = await this.$refs.chatbox.sendChatMessage(this.$refs.chatbox.userInput, this.backendUrl);
      if (stream) {
        const lastIndex = this.chatHistory.length - 1;

        let streamMessage = "";
        await this.$refs.chatbox.streamMessage(stream, (chunk) => {
          streamMessage += chunk;
          this.chatHistory[lastIndex].message = streamMessage;
        });
      }
    }
  }
}

</script>


<style>
.convo-title {
  display: flex;
  justify-content: center;
  font-size: 50px;
  background-color: rgba(255, 209, 248, 0.88);
  margin-top: 10px;
  margin-left: 100px;
  margin-right: 100px;
  border-radius: 25px;
}

/* default chat message */
.chat-message {
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
.chat-message.left {
  margin-right: auto;
  margin-left: 10px;
}

/* align chat to right */
.chat-message.right {
  margin-left: auto;
  margin-right: 10px;
  background-color: rgb(79, 195, 247)
}


.history {
  position: fixed;
  bottom: 40px;
  right: 40px;
  width: 1000px;
  height: 1650px;
  padding: 10px;
  border-color: black;
  border-radius: 20px;
  font-size: 16px;
  background-color: rgb(217, 139, 166, 0.88);
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 5fr 1fr;
  gap: 0px 0px;
  grid-template-areas:
    "title title title"
    "conversation conversation conversation"
    "footer footer footer";
}

.inner {
  margin-top: 20px;
  min-height: 200px;
  max-height: 1000px;
}

.title {
  grid-area: title;
}

.conversation {
  grid-area: conversation;
  overflow: hidden;
  overflow-y: auto;
}

.footer {
  grid-area: footer;
}
</style>
