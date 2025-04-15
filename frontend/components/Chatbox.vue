<template>
  <div class="chatbox">
    <ul>
      <!-- <li id="buttons" @click="therapistChat"><a href="#">Anne Alysis</a></li> -->
    </ul>
    <textarea id="userInput" v-model="userInput" placeHolder="Type something here..."
      @keydown.enter.exact.prevent="sendMessage" @keydown.shift.enter="addNewLine" rows="5">
    </textarea>
    <button id="btn-chat-send" @click="sendMessage">Send</button>
  </div>
</template>


<script>


export default {
  name: "Chatbox",

  data() {
    return {
      userInput: "",
    };
  },

  methods: {

    sendMessage() {
      this.$emit("message-sent", this.userInput);
      this.userInput = "";
    },

    addNewLine() {
      this.userInput += "\n";
    },

    async sendChatMessage(chatMessage, url) {
      const response = await fetch(`${url}/chat`,
        {
          method: "POST",
          headers: { "Access-Control-Allow-Origin": "*", "Content-Type": "application/json" },
          body: JSON.stringify({
            message: chatMessage
          })
        }
      );

      if (!response) {
        console.error("Failed to fetch the stream data");
        return;
      }

      const stream = response.body;
      return stream
    },

    async sendIntroduction(url) {
      const response = await fetch(`${url}/intro`,
        {
          headers: { "Access-Control-Allow-Origin": "*" }
        }
      );

      if (!response) {
        console.error("Failed to fetch the stream data");
        return;
      }

      const stream = response.body;
      return stream
    },

    async streamMessage(stream, onChunk) {
      console.log("calling the chat api")
      // const response = await fetch('http://localhost:8000/intro',
      //   {
      //     headers: { "Access-Control-Allow-Origin": "*" }
      //   }
      // );
      //
      // if (!response) {
      //   console.error("Failed to fetch the stream data");
      //   return;
      // }
      //
      // const stream = response.body;

      if (stream) {

        const reader = stream.getReader();
        const decoder = new TextDecoder();

        let done = false;

        this.userInput = ""
        while (!done) {
          const { value, done: isDone } = await reader.read();
          done = isDone;

          const chunk = decoder.decode(value, { stream: true });
          console.log(chunk);
          if (chunk && onChunk) {
            onChunk(chunk);
          }
        }
      }
    },
  }
}

</script>


<style>
.chatbox {
  position: absolute;
  bottom: 20px;
  width: 880px;
}

#btn-chat-send {
  position: absolute;
  width: 75px;
  height: 75px;
  border-radius: 50%;
  bottom: 20px;
  right: -100px;
  background-color: rgb(104, 193, 234);
}

#userInput {
  width: 100%;
  /* Make the textarea take the full width of the parent */
  height: 90%;
  font-size: 28px;
  /* Font size for the textarea */
  padding-left: 20px;
  /* Padding inside the textarea */
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 95px;
  resize: none;
  /* Disable resizing */
  border-radius: 10px;
  outline: none;
  background-color: rgba(255, 209, 248, 0.88);
  border: 3px solid black;
  color: black;
}



ul {
  list-style: none;
  display: flex;
  justify-content: center;
  /* Center the buttons horizontally */
  float: left;
  gap: 10px;
  /* Space between buttons */
}

ul li {
  display: inline-block;
}

ul li a {
  text-decoration: none;
  padding: 10px;
  padding-left: 30px;
  padding-right: 30px;
  border-radius: 5px;
  /* Rounded buttons */
  font-size: 26px;
  background-color: rgba(255, 209, 248, 0.88);
  border: 3px solid black;
  color: black;
}

ul li a:hover {
  background-color: #888;
  /* Hover effect */
}
</style>
