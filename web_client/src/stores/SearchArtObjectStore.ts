import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const useSerchArtObjectStore = defineStore('SerchArtObjectStore', () => {
  const searchItem = reactive<
    Partial<{
      title: string;
      description: string;
      image: File;
      imageUrl: string;
      path: string;
      category: string;
    }>
  >({});

  // watch(
  //   () => searchItem.image,
  //   () => {
  //     console.log('image changed');
      
  //   }
  // );

  const uploadImage = async () => {
    const formData = new FormData();

    if (searchItem?.image) {
      formData.append('file', searchItem.image);
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to upload image');
      }

      const data = await response.json();
      searchItem.path = data.path;
      // searchItem.category = data.category;
      return data;
    }

    return null;
  };

  return {
    searchItem,
    uploadImage,
  };
});
