import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const useAddArtObjectStore = defineStore('AddArtObjectStore', () => {
  const addItem = reactive<Partial<{
    title: string;
    description: string;
    image: File;
    imageUrl: string;
    path: string;
    category: string;
  }>>({});

  const uploadImage = async () => {
    const formData = new FormData();

    if (addItem?.image) {
      formData.append('file', addItem.image);
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      addItem.path = data.path;
      return data;
    }

    return null;
  };

  const createItem = async () => {
    if (
      addItem?.title &&
      addItem?.description &&
      addItem?.path &&
      addItem?.category
    ) {
      const response = await fetch('/api/add_image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: addItem.title,
          description: addItem.description,
          path: addItem.path,
          category: addItem.category,
        }),
      });
      const data = await response.json();
      console.log(data);
      return data;
    }
    throw new Error('Invalid input');
  };

  return {
    addItem,
    uploadImage,
    createItem,
  };
});
