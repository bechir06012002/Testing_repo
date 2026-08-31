import type { User } from "../types";

interface UserCardProps {
  user: User;
  onSelect?: (id: number) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  return (
    <div className="user-card" onClick={() => onSelect?.(user.id)}>
      <span>{user.email}</span>
      {user.isAdmin && <span className="badge">admin</span>}
    </div>
  );
}
