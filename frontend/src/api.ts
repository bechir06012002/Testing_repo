import type { Order, User } from "./types";

const BASE_URL = "/api";

export async function fetchUser(id: number): Promise<User> {
  const res = await fetch(`${BASE_URL}/users/${id}`);
  return res.json();
}

export async function fetchOrders(userId: number): Promise<Order[]> {
  const res = await fetch(`${BASE_URL}/users/${userId}/orders`);
  return res.json();
}
