export interface User {
  id: number;
  email: string;
  isAdmin: boolean;
  tags: string[];
}

export interface Order {
  id: number;
  userId: number;
  amountCents: number;
  status: "pending" | "paid" | "cancelled";
}
