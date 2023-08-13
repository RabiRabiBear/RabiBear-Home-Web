<!-- <template>
    <div class="todo-list">
      <h2>{{ title }}</h2>
      <ul>
        <li v-for="(item, index) in todoItems" :key="index">
          <div class="item-header" @click="toggleSection(item)">
            <el-checkbox
              v-model="item.checked"
              @change="handleChange(item)"
              :disabled="!isAdmin"
            >
              {{ item.text }}
            </el-checkbox>
            <i :class="['el-icon-arrow-right', { 'expanded': item.expanded }]"></i>
          </div>
          <div v-if="item.expanded" class="item-section">
            <div class="section-content">
              <div class="section-date">{{ item.date }}</div>
              <div class="section-text">{{ item.sectionText }}</div>
              <el-image
                v-if="item.sectionImage"
                :src="item.sectionImage"
                :fit="fitMode"
                class="section-image"
              ></el-image>
              <div class="section-actions" v-if="isAdmin">
                <el-button type="primary" size="small" @click="editSection(item)">
                  Edit
                </el-button>
              </div>
            </div>
            <el-dialog v-model="editDialogVisible" title="Edit Section" :append-to-body="true">
              <el-form ref="editForm" :model="editForm" label-position="top">
                <el-form-item label="Date">
                  <el-date-picker v-model="editForm.date" type="date" placeholder="Select date"></el-date-picker>
                </el-form-item>
                <el-form-item label="Text">
                  <el-input v-model="editForm.text" type="textarea" rows="3"></el-input>
                </el-form-item>
                <el-form-item label="Image">
                  <el-upload
                    class="upload-demo"
                    :action="uploadUrl"
                    :on-success="handleUploadSuccess"
                    :show-file-list="false"
                    accept="image/*"
                  >
                    <el-button size="small" type="primary">Upload</el-button>
                  </el-upload>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="saveSection">Save</el-button>
                </el-form-item>
              </el-form>
            </el-dialog>
          </div>
        </li>
      </ul>
    </div>
  </template>


<script>
import { ref } from 'vue';
import { API_BASE_URL } from '@/config.js';

export default {
  data() {
    return {
      title: "Todo List",
      todoItems: [
        { text: "Item 1", checked: false, expanded: false, date: "", sectionText: "", sectionImage: "" },
        { text: "Item 2", checked: false, expanded: false, date: "", sectionText: "", sectionImage: "" },
        { text: "Item 3", checked: false, expanded: false, date: "", sectionText: "", sectionImage: "" },
      ],
      isAdmin: true,
      editDialogVisible: false,
      editForm: {
        date: "",
        text: "",
        image: null,
      },
      fitMode: "cover",
      uploadUrl: `${API_BASE_URL}`,
    };
  },
  methods: {
    toggleSection(item) {
      item.expanded = !item.expanded;
    },
    handleChange(item) {
      if (!this.isAdmin) {
        alert("You are not allowed to change the item status.");
        item.checked = !item.checked; // Reset the checkbox state
      }
    },
    editSection(item) {
      this.editForm.date = item.date;
      this.editForm.text = item.sectionText;
      this.editForm.image = null;
      this.editDialogVisible = true;
    },
    saveSection() {
      // Here, you would typically send the edited section data to the server for saving
      // You can access the edited data from `this.editForm`
      // Replace the following console.log with your server API call
      console.log("Save section:", this.editForm);

      this.editDialogVisible = false;
    },
    handleUploadSuccess(response) {
      // Handle the image upload success
      // The response contains the URL or details of the uploaded image
      // You can update `this.editForm.image` with the received URL or relevant data
      console.log("Upload success:", response);
    },
  },
};
</script> -->
<template>
  <div class="todo-list">
    <h2 class="title">{{ title }}</h2>
    <ul>
      <li v-for="(item,idx, index) in todoItems" :key="index" style="list-style-type:none;">
        <el-card class="item_card" shadow="hover" :body-style="{ padding: '0.1rem' }">
          <!-- <el-checkbox v-model="item.isdone" size="large" :disabled="!isAdmin" style="padding-left: 1rem;" > -->
            <el-checkbox v-model="item.isdone" size="large" style="padding-left: 1rem;" @click="handleCheckboxClick" class="checkbox"> 
            <!-- {{ item.content }} -->
            <!-- <span class="custom-checkbox-text">{{ item.content }}</span> -->
            <span v-if="item.isdone" class="checked-text">{{ item.content }}</span>
      <span v-else>{{ item.content }}</span>
          </el-checkbox>
        </el-card>

      </li>
    </ul>
  </div>
</template>
  
<script>
import { ref } from 'vue';
import Cookies from 'js-cookie';
import axios from "axios";
import { API_BASE_URL } from '@/config.js';

export default {
  data() {
    return {
      // title: "如果说这一生有一件事最幸运 就是赌中亿分之一的机率遇见你",
      title: "如果說這一生有一件事最幸運💖 \n 就是賭中億分之一的機率遇見你",
      todoItems: [
        // { text: "Item 1", checked: false },
        // { text: "Item 2", checked: false },
        // { text: "Item 3", checked: false },
      ],
      isAdmin: ref(['rabbit', 'bear'].includes(Cookies.get('username'))),
    };
  },
  watch: {
    todoItems: {
      handler(newVal, oldVal) {
        if (this.isAdmin) {
          this.updateCheckInfo();
        }
      },
      deep: true
    }
  },
  methods: {
    handleCheckboxClick(event, item) {
      if (!this.isAdmin) {
        event.preventDefault(); // Prevent the default click behavior
      }
    },
    updateCheckInfo() {
      axios.post(`${API_BASE_URL}/update_100things`, this.todoItems)
    },
  },
  created() {
    axios.get(`${API_BASE_URL}/get_100things`, {
      headers: { 'Content-Type': 'application/json' },
      params: {},
    })
      .then((response) => {
        this.todoItems = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  }


};
</script>
  
<style>
@import '@/assets/fonts/fonts.css';

.todo-list {
  margin: 2rem;
  /* text-align: center; */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.item_card {
  height: 2.5rem;
  margin: 0.5rem;
  width: 40rem;
}

.title {
  font-family: 'OZJiaotangxiawucha', sans-serif;
  white-space: pre-wrap;
  margin-bottom: 1rem;
}
.checkbox {
  font-family: 'QTXiaotu', sans-serif;
}

.checkbox .el-checkbox__input.is-checked .el-checkbox__inner {
  background-color: #f596aa;/* Change this to your desired color */
  border-color: #f596aa; /* Change this to your desired color */
}

.checkbox .checked-text {
  color: #f596aa; /* Change this to your desired text color */
}

</style>
  