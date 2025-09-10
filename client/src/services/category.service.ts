import axios from "@/libs/configs/axios";

export type Category = {
  id: string;
  name: string;
};

export const getCategories = async (): Promise<Category[]> => {
  const response = await axios.get("/categories");
  return response.data;
};
