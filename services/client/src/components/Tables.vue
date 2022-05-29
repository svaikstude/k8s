<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Shop</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.table-modal>Add Table</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Manufacturer</th>
              <th scope="col">Model</th>
              <th scope="col">Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(table, index) in Tables" :key="index">
              <td>{{ table.title }}</td>
              <td>{{ table.author }}</td>
              <td>
                <span v-if="table.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button
                        type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.table-update-modal
                        @click="editTable(table)">
                    Update
                </button>
                <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteTable(table)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTableModal"
             id="table-modal"
             title="Add a new table"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-manufacturer-group"
                    label="Manufacturer:"
                    label-for="form-manufacturer-input">
          <b-form-input id="form-manufacturer-input"
                        type="text"
                        v-model="addTableForm.manufacturer"
                        required
                        placeholder="Enter manufacturer">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-model-group"
                      label="Model:"
                      label-for="form-model-input">
            <b-form-input id="form-model-input"
                          type="text"
                          v-model="addTableForm.model"
                          required
                          placeholder="Enter model">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-price-group"
                      label="Price:"
                      label-for="form-price-input">
            <b-form-input id="form-price-input"
                          type="text"
                          v-model="addTableForm.price"
                          required
                          placeholder="Enter price">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-photo-group"
                      label="Photo URL:"
                      label-for="form-photo-input">
            <b-form-input id="form-photo-input"
                          type="text"
                          v-model="addTableForm.photo"
                          required
                          placeholder="Enter photo">
            </b-form-input>
          </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editTableModal"
             id="table-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-manufacturer-group"
                    label="Manufacturer:"
                    label-for="form-manufacturer-input">
          <b-form-input id="form-manufacturer-input"
                        type="text"
                        v-model="addTableForm.manufacturer"
                        required
                        placeholder="Enter manufacturer">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-model-group"
                      label="Model:"
                      label-for="form-model-input">
            <b-form-input id="form-model-input"
                          type="text"
                          v-model="addTableForm.model"
                          required
                          placeholder="Enter model">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-price-group"
                      label="Price:"
                      label-for="form-price-input">
            <b-form-input id="form-price-input"
                          type="text"
                          v-model="addTableForm.price"
                          required
                          placeholder="Enter price">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-photo-group"
                      label="Photo URL:"
                      label-for="form-photo-input">
            <b-form-input id="form-photo-input"
                          type="text"
                          v-model="addTableForm.photo"
                          required
                          placeholder="Enter photo">
            </b-form-input>
          </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      Tables: [],
      addTableForm: {
        manufacturer: '',
        model: '',
        price: 0,
        photo: '',
      },
      editForm: {
        id: '',
        manufacturer: '',
        model: '',
        price: 0,
        photo: '',
      },
      message: '',
      showMessage: false,
      ROOT_API: process.env.ROOT_API,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTables() {
      const path = `${this.ROOT_API}/tables`;
      axios.get(path)
        .then((res) => {
          this.Tables = res.data.Tables;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTable(payload) {
      const path = `${this.ROOT_API}/tables`;
      axios.post(path, payload)
        .then(() => {
          this.getTables();
          this.message = 'Table added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTables();
        });
    },
    updateTable(payload, tableID) {
      const path = `${this.ROOT_API}/tables/${tableID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTables();
          this.message = 'Table updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTables();
        });
    },
    removeTable(tableID) {
      const path = `${this.ROOT_API}/tables/${tableID}`;
      axios.delete(path)
        .then(() => {
          this.getTables();
          this.message = 'Table removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTables();
        });
    },
    initForm() {
      this.addTableForm.manufacturer = '';
      this.addTableForm.model = '';
      this.addTableForm.photo = '';
      this.addTableForm.price = 0;
      this.editForm.id = '';
      this.editForm.manufacturer = '';
      this.editForm.model = '';
      this.editForm.photo = '';
      this.editForm.price = 0;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTableModal.hide();
      let read = false;
      if (this.addTableForm.read[0]) read = true;
      const payload = {
        manufacturer: this.addTableForm.manufacturer,
        model: this.addTableForm.model,
        photo: this.addTableForm.photo,
        price: this.addTableForm.price,
      };
      this.addTable(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTableModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        manufacturer: this.editForm.manufacturer,
        model: this.editForm.model,
        photo: this.editForm.photo,
        price: this.editForm.price,
      };
      this.updateTable(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTableModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTableModal.hide();
      this.initForm();
      this.getTables(); // why?
    },
    onDeleteTable(table) {
      this.removeTable(table.id);
    },
    editTable(table) {
      this.editForm = table;
    },
  },
  created() {
    this.getTables();
  },
};
</script>
