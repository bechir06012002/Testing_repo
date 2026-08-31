export function formatCents(amountCents: number): string {
  return `$${(amountCents / 100).toFixed(2)}`;
}

export function truncate(value: string, maxLength: number): string {
  if (value.length <= maxLength) {
    return value;
  }
  return `${value.slice(0, maxLength)}...`;
}
