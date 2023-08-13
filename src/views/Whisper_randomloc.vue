<!-- <template>
    <div class="message-board">
      <el-container>
        <el-main>
          <el-row>
            <el-col :span="8" v-for="(message, index) in messages" :key="index">
              <el-card>
                <div slot="header" class="clearfix">
                  <el-avatar :size="40" :src="message.avatar"></el-avatar>
                  <span>{{ message.userName }}</span>
                </div>
                <div class="message-box">
                  <p class="message-text">{{ message.message }}</p>
                  <p class="publish-time">{{ message.publishTime }}</p>
                  <p class="time-zone">{{ message.timeZone }}</p>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
      <div class="message-input" v-if="isLoggedIn">
        <el-input v-model="newMessage" type="textarea" placeholder="Enter your message"></el-input>
        <el-button @click="submitMessage">Submit</el-button>
      </div>
    </div>
  </template>
  
  <script>
  import { ElAvatar, ElButton, ElCard, ElCol, ElContainer, ElInput, ElMain, ElRow } from 'element-plus';
  
  export default {
    components: {
      ElAvatar,
      ElButton,
      ElCard,
      ElCol,
      ElContainer,
      ElInput,
      ElMain,
      ElRow,
    },
    data() {
      return {
        messages: [
          {
            avatar: 'path/to/avatar1.png',
            userName: 'User1',
            publishTime: '2023-08-12 10:00 AM',
            timeZone: 'UTC+1',
            message: 'This is the first message.',
          },
          {
          avatar: 'path/to/avatar2.png',
          userName: 'User2',
          publishTime: '2023-08-12 11:30 AM',
          timeZone: 'UTC-5',
          message: 'This is a longer message that will take up more space in the message box.',
        },
        {
          avatar: 'path/to/avatar3.png',
          userName: 'User3',
          publishTime: '2023-08-12 1:45 PM',
          timeZone: 'UTC+3',
          message: 'Short message.',
        },
          // ... other messages ...
        ],
        newMessage: '',
      };
    },
    computed: {
      isLoggedIn() {
        // Check if the user is logged in (you can implement your own logic here)
        return this.getUserFromCookie() !== null;
      },
    },
    methods: {
      getUserFromCookie() {
        // Implement logic to read user data from cookie
        // Return an object with userName and avatar properties
        return {
          userName: 'LoggedUser',
          avatar: 'path/to/cookie/avatar.png',
        };
      },
      submitMessage() {
        if (!this.newMessage.trim()) {
          return;
        }
  
        const user = this.getUserFromCookie();
        if (user) {
          const newMessage = {
            avatar: user.avatar,
            userName: user.userName,
            publishTime: new Date().toLocaleString(),
            timeZone: 'UTC', // You can adjust the time zone
            message: this.newMessage,
          };
  
          this.messages.push(newMessage);
          this.newMessage = '';
        }
      },
    },
  };
  </script>
  
  <style>
  .clearfix::after {
    content: '';
    display: table;
    clear: both;
  }
  
  .message-box {
    margin-top: 10px;
  }
  
  .publish-time,
  .time-zone {
    font-size: 12px;
    color: #999;
    margin-top: 5px;
  }
  
  .message-input {
    margin-top: 20px;
  }
  
  .message-text {
    word-wrap: break-word; /* Add this line to handle long messages */
  }
  </style>
   -->


   <template>
    <div class="card-grid">
      <el-row justify="space-between">
        <el-col :span="8">
          <el-card :class="cardClasses(index, cardIndex)" v-for="(item, index) in column1Items" :key="index">
            {{ item.content }}
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :class="cardClasses(index, cardIndex)" v-for="(item, index) in column2Items" :key="index">
            {{ item.content }}
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :class="cardClasses(index, cardIndex)" v-for="(item, index) in column3Items" :key="index">
            {{ item.content }}
          </el-card>
        </el-col>
      </el-row>
    </div>
  </template>

<style>
  .card-grid {
    display: flex;
    flex-direction: column;
  }

  .el-col {
    padding: 0 2em; /* Adjust the value to control the overlap */
  }


  .float-left {
      margin-right: 2em;
      margin-top: 2em;
    }
  
    .float-right {
      margin-left: 2em;
      margin-top: 1em;
    }
</style>

<script>
export default {
  data() {
    return {
      column1Items: [
        { content: 'Card 1' },
        { content: 'Card 2 Card 2Card 2Card 2Card 2Card 2Card 2Card 2Card 2Card 2' },
        { content: 'Card 3' },
        /* ... */
      ],
      column2Items: [
        { content: 'Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4' },
        { content: 'Card 5' },
        { content: 'Card 6' },
        /* ... */
      ],
      column3Items: [
        { content: 'Card 7' },
        { content: 'Card 8' },
        { content: 'Card 9' },
        /* ... */
      ],
    };
  },
  methods: {
    cardClasses(rowIndex, cardIndex) {
        return {
          'float-left': rowIndex % 2 === 0, // Apply this class for odd rows
          'float-right': rowIndex % 2 === 1, // Apply this class for even rows
        };
      },
  }
};
</script>




<!-- <template>
    <div class="card-grid">
      <el-row v-for="(row, index) in cardRows" :key="index">
        <el-col :span="8" v-for="(card, cardIndex) in row" :key="cardIndex">
          <el-card :class="cardClasses(index, cardIndex)">
            {{ card.content }}
          </el-card>
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        columnItems: [
        { content: 'Card 1' },
        { content: 'Card 2 Card 2Card 2Card 2Card 2Card 2Card 2Card 2Card 2Card 2' },
        { content: 'Card 3' },
        { content: 'Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4Card 4' },
        { content: 'Card 5' },
        { content: 'Card 6' },
        { content: 'Card 7' },
        { content: 'Card 8' },
        { content: 'Card 9' },
        /* ... */
      ],
      };
    },
    methods: {
      cardClasses(rowIndex, cardIndex) {
        return {
          'float-left': rowIndex % 2 === 0, // Apply this class for odd rows
          'float-right': rowIndex % 2 === 1, // Apply this class for even rows
        };
      },
    },
    computed: {
      cardRows() {
        const cardsPerRow = 3; // Maximum number of cards per row
      const rows = [];

      for (let i = 0; i < this.columnItems.length; i += cardsPerRow) {
        const row = [];

        for (let j = i; j < i + cardsPerRow; j++) {
          if (this.columnItems[j]) {
            row.push(this.columnItems[j]);
          }
        }

        rows.push(row);
      }

      return rows;
      },
    },
  };
  </script>
  
  <style>
    .card-grid {
        display: flex;
    flex-direction: column;
    }

    .card {
    margin-top: 2em; /* Adjust the value to control the overlap */
    width: 10em;
  }
  
    .float-left {
      margin-right: 2em;
    }
  
    .float-right {
      margin-left: 2em;
    }
  </style>
   -->