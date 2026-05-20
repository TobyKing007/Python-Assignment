package data.repositories;

import data.models.Guest;

public interface GuestRepository {

    Guest save (Guest guest);
    Guest findById(int id);
    void deleteById(int id);
    int count();
}
