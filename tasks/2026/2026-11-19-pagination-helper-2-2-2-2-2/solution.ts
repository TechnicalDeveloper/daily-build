export type PageOptions = { page?: number; pageSize?: number };

export type Paginated<T> = {
  items: T[];
  totalItems: number;
  totalPages: number;
  currentPage: number;
  pageSize: number;
  hasNext: boolean;
  hasPrev: boolean;
};

export function paginate<T>(items: T[], options: PageOptions = {}): Paginated<T> {
  const pageSize = options.pageSize && options.pageSize > 0 ? options.pageSize : 10;
  const totalItems = items.length;
  const totalPages = totalItems === 0 ? 0 : Math.ceil(totalItems / pageSize);

  let page = options.page ?? 1;
  if (page < 1) page = 1;

  if (totalPages === 0) {
    page = 1;
  } else if (page > totalPages) {
    page = totalPages;
  }

  const startIndex = (page - 1) * pageSize;
  const pageItems = totalPages === 0 ? [] : items.slice(startIndex, startIndex + pageSize);

  return {
    items: pageItems,
    totalItems,
    totalPages,
    currentPage: page,
    pageSize,
    hasNext: page < totalPages,
    hasPrev: page > 1 && totalItems > 0,
  };
}
