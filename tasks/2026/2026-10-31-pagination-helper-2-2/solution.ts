export interface PaginatedResult<T> {
  items: T[];
  totalItems: number;
  totalPages: number;
  currentPage: number;
  pageSize: number;
  hasPrev: boolean;
  hasNext: boolean;
}

export function paginate<T>(
  items: T[],
  page: number,
  pageSize: number
): PaginatedResult<T> {
  if (pageSize <= 0) {
    throw new Error("pageSize must be greater than zero");
  }
  const totalItems = items.length;
  const totalPages = Math.max(1, Math.ceil(totalItems / pageSize));
  const currentPage = Math.max(1, Math.min(page, totalPages));
  const startIndex = (currentPage - 1) * pageSize;
  const endIndex = Math.min(startIndex + pageSize, totalItems);
  const slicedItems = items.slice(startIndex, endIndex);
  return {
    items: slicedItems,
    totalItems,
    totalPages,
    currentPage,
    pageSize,
    hasPrev: currentPage > 1,
    hasNext: currentPage < totalPages,
  };
}
