export interface PaginationParams {
  page?: number;
  pageSize?: number;
  totalItems: number;
}

export interface PaginationResult {
  page: number;
  pageSize: number;
  totalItems: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  startIndex: number;
  endIndex: number; // exclusive
}

export function paginate(params: PaginationParams): PaginationResult {
  const { totalItems } = params;
  const rawPage = params.page ?? 1;
  const rawPageSize = params.pageSize ?? 10;

  // Normalize page
  let page = Math.floor(rawPage);
  if (!Number.isFinite(page) || page < 1) {
    page = 1;
  }

  // Normalize pageSize
  let pageSize = Math.floor(rawPageSize);
  if (!Number.isFinite(pageSize) || pageSize < 1) {
    pageSize = 1;
  }

  const totalPages = totalItems === 0 ? 0 : Math.ceil(totalItems / pageSize);

  // Clamp page to valid range
  if (totalPages > 0) {
    if (page > totalPages) {
      page = totalPages;
    }
  } else {
    page = 1;
  }

  const startIndex = (page - 1) * pageSize;
  const endIndex = Math.min(startIndex + pageSize, totalItems);

  return {
    page,
    pageSize,
    totalItems,
    totalPages,
    hasNextPage: page < totalPages,
    hasPreviousPage: page > 1 && totalPages > 0,
    startIndex,
    endIndex,
  };
}
