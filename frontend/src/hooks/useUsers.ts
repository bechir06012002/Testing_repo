import { useEffect, useState } from "react";
import { fetchUser } from "../api";
import type { User } from "../types";

export function useUser(id: number) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetchUser(id).then((u) => {
      setUser(u);
      setLoading(false);
    });
  }, [id]);

  return { user, loading };
}
